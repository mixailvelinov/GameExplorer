from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import status

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from games.forms import GameReviewForm, GameForm, DeleteGame
from games.models import Game, Review
from GameExplorer.permissions import IsModerator, IsAdmin
from games.serializers import GameSerializer, ReviewSerializer


class GamesListView(ListView):
    model = Game
    template_name = 'games/games-list.html'

    def get_queryset(self):
        return Game.objects.all().order_by('-release_date')[:3]


class AllGamesView(ListView):
    model = Game
    template_name = 'games/all-games.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Game.objects.all()
        query = self.request.GET.get('search_form')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game-details-view.html'

    def get_context_data(self, **kwargs):
        game = get_object_or_404(Game, slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['total_rating'] = game.review_set.all().aggregate(Avg('rating'))['rating__avg']
        return context


class GameReview(LoginRequiredMixin, CreateView):
    model = Review
    form_class = GameReviewForm
    template_name = 'games/game-review.html'

    def form_valid(self, form):
        game = get_object_or_404(Game, slug=self.kwargs['slug'])

        if Review.objects.filter(game=game, user=self.request.user).exists():
            messages.error(self.request, 'You have already reviewed this game!')
            return self.form_invalid(form)

        form.instance.game = game
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('games-detail', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context


class EditGameReview(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'games/game-review.html'
    form_class = GameReviewForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('games-detail', kwargs={'slug': self.kwargs['slug']})

    def get_object(self, queryset=None):
        review = Review.objects.get(id=self.kwargs['id'])
        if review.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this review.")
        return review


class DeleteGameReview(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'games/game-review-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('games-list')

    def get_object(self, queryset=None):
        review = get_object_or_404(Review, id=self.kwargs['id'])
        if not self.request.user.is_staff:
            if review.user != self.request.user:
                raise PermissionDenied("You do not have permission to delete this review.")
        return review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context


class AddGame(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/add-game.html'

    def get_success_url(self):
        return reverse_lazy('games-detail', kwargs={'slug': self.object.slug})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class EditGame(UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'games/add-game.html'

    def get_success_url(self):
        return reverse_lazy('games-detail', kwargs={'slug': self.object.slug})

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


def delete_game(request, slug):
    game = Game.objects.get(slug=slug)
    form = DeleteGame(instance=game)

    if not request.user.is_superuser:
        return redirect('index')

    if request.method == 'POST':
        game.delete()
        return redirect('games-list')

    context = {'game': game, 'form': form}
    return render(request, 'games/delete-game.html', context)


#API
class GameListAllReviews(ListView):
    template_name = 'games/game-all-reviews.html'
    paginate_by = 5

    def get_queryset(self):
        game = get_object_or_404(Game, slug=self.kwargs['slug'])
        return Review.objects.filter(game=game)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context


class ManageGameAPIView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, *args, **kwargs):
        try:
            game = Game.objects.get(slug=kwargs['slug'])
        except Game.DoesNotExist:
            return Response({"detail": "This game hasn't been added yet."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            game_instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            game = Game.objects.get(slug=kwargs['slug'])
        except Game.DoesNotExist:
            return Response({'detail': 'Game not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            game = Game.objects.get(slug=kwargs['slug'])
        except Game.DoesNotExist:
            return Response({"detail": "Game not found."}, status=status.HTTP_404_NOT_FOUND)

        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManageReviewAPIView(RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsModerator]
    lookup_field = 'id'


class ListAllGameReviewsAPIView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsModerator]

    def get_queryset(self):
        game_slug = self.kwargs.get('slug')
        return Review.objects.filter(game__slug=game_slug)
