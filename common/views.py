from django.shortcuts import render

from accounts.models import Profile


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

    context = {
        'account': account,
        'profile': profile,
    }
    return render(request, 'common/index.html', context)