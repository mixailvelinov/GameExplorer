from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from accounts.models import Profile
from common.forms import GameSuggestionForm, AddPlatformForm, AddGenreForm
from common.models import GameSuggestion, Platform, Genre
from games.models import Game

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
    success_url = reverse_lazy('suggestion-create')

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


#Admin only views
class CreatePlatform(LoginRequiredMixin, CreateView):
    model = Platform
    form_class = AddPlatformForm
    template_name = 'common/create-platform.html'
    success_url = reverse_lazy('add-platform')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Platform added and can be assigned to games.")

        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)


class CreateGenre(LoginRequiredMixin, CreateView):
    model = Genre
    form_class = AddGenreForm
    template_name = 'common/create-genre.html'
    success_url = reverse_lazy('add-genre')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Genre added and can be assigned to games.")

        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)


class GameSuggestionsList(LoginRequiredMixin, ListView):
    model = GameSuggestion
    template_name = 'common/view-game-suggestions.html'
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)


def delete_game_suggestion(request, id):
    game = GameSuggestion.objects.get(id=id)

    if not request.user.is_superuser or game is None:
        return redirect('index')

    if request.method == 'POST':
        game.delete()
        return redirect('game-suggestions-list')

    context = {'game': game}

    return render(request, 'common/view-game-suggestions.html', context)
