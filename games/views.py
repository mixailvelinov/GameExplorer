from django.shortcuts import render
from django.views.generic import ListView, DetailView

from games.models import Game


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
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context
