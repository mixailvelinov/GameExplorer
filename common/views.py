from django.shortcuts import render

from accounts.models import Profile


# Create your views here.


def index(request):
    account = request.user
    profile = Profile.objects.get(user=account)
    context = {
        'account': account,
        'profile': profile,
    }
    return render(request, 'common/index.html', context)