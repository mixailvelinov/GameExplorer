from django.db.models import Avg, Sum
from django.db.models.functions import Coalesce
from django.forms import FloatField
from django.shortcuts import render

from accounts.models import Profile
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

