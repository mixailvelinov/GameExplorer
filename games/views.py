from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import  Avg
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from games.forms import GameReviewForm
from games.models import Game, Review
from GameExplorer.permissions import IsModerator, IsAdmin
from games.serializers import GameSerializer, ReviewSerializer


class GamesListView(ListView):
    model = Game
    template_name = 'games/games-list.html'

    def get_queryset(self):
        return Game.objects.all().order_by('-release_date')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game-details-view.html'

    def get_context_data(self, **kwargs):
        game = get_object_or_404(Game, slug=self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
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
        context['account'] = self.request.user
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context


class EditGameReview(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'games/game-review.html'
    form_class = GameReviewForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('games-detail', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context

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
        if review.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this review.")
        return review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context

#API
class GameListAllReviews(ListView):
    template_name = 'games/game-all-reviews.html'
    paginate_by = 5

    def get_queryset(self):
        game = get_object_or_404(Game, slug=self.kwargs['slug'])
        return Review.objects.filter(game=game)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        context['game'] = Game.objects.get(slug=self.kwargs['slug'])
        return context


class GamesViewAPI(APIView):
    def get(self, req):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        permission_classes = [IsModerator]
        return Response({'games': serializer.data})


class UpdateExistingGame(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'slug'
    permission_classes = [IsModerator]


class DeleteExistingGame(RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'slug'


class GameCreateApiView(CreateAPIView):
    model = Game
    serializer_class = GameSerializer
    permission_classes = [IsAdmin]


class ModifyReviewAPIView(RetrieveUpdateDestroyAPIView):
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
