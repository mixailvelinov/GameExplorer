from django.contrib import messages
from django.db.models import Sum, Avg
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from games.forms import GameReviewForm
from games.models import Game, Review


# Create your views here.

class GamesListView(ListView):
    model = Game
    template_name = 'games/games-list.html'

    def get_queryset(self):
        return Game.objects.all()[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context


class AllGamesView(ListView):
    model = Game
    template_name = 'games/all-games.html'

    def get_queryset(self):
        return Game.objects.all()

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


class GameReview(CreateView):
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
        return context




