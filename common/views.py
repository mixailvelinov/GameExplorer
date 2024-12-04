from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView

from accounts.models import Profile
from common.forms import GameSuggestionForm
from common.models import GameSuggestion, Platform, Genre
from common.serializers import PlatformSerializer, GenreSerializer
from games.models import Game

from GameExplorer.permissions import IsModerator, IsAdmin

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        account = request.user
        try:
            profile = Profile.objects.get(user=account)
        except Profile.DoesNotExist:
            profile = None
    else:
        account = None
        profile = None

    latest_game = Game.objects.order_by('-release_date').first()

    top_game = Game.objects.annotate(
        average_rating=Avg('review__rating')
    ).filter(average_rating__isnull=False).order_by('-average_rating').first()

    games = Game.objects.all()

    context = {
        'account': account,
        'profile': profile,
        'latest_game': latest_game,
        'top_game': top_game,
        'games': games,
    }
    return render(request, 'common/index.html', context)


class GameSuggestionCreate(LoginRequiredMixin, CreateView):
    model = GameSuggestion
    form_class = GameSuggestionForm
    template_name = 'common/game-suggestion-page.html'
    success_url = reverse_lazy('suggestion_create')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        messages.success(self.request, "Thank you! Your suggestion has been submitted and is under review.")

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context