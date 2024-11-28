from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Avg, Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from games.forms import GameReviewForm
from games.models import Game, Review

# Create your views here.


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
    paginate_by = 8

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
            raise Exception('You have already reviewed this game!')

        form.instance.game = game
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('games-detail', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        context['game'] = game = Game.objects.get(slug=self.kwargs['slug'])
        return context


class GameListAllReviews(ListView):
    template_name = 'games/game-all-reviews.html'
    paginate_by = 5

    def get_queryset(self):
        game = get_object_or_404(Game, slug=self.kwargs['slug'])
        return Review.objects.filter(game=game)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        context['game'] = game = Game.objects.get(slug=self.kwargs['slug'])
        return context

