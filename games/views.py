from django.shortcuts import render
from django.views.generic import ListView

from games.models import Game


# Create your views here.

class GamesListView(ListView):
    model = Game
    template_name = 'games/games-list.html'

    def get_queryset(self):
        return Game.objects.all()[:3]


class AllGamesView(ListView):
    model = Game
    template_name = 'games/all-games.html'

    def get_queryset(self):
        return Game.objects.all()
