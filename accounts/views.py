from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from accounts.forms import AccountRegisterForm, AccountLoginForm, AccountEditForm
from accounts.models import Account, Profile
from games.models import Review


# Create your views here.


class AccountRegisterView(CreateView):
    model = Account
    form_class = AccountRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/register-page.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class AccountLoginView(LoginView):
    form_class = AccountLoginForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class AccountLogoutView(LogoutView):
    pass


@login_required
def account_details(request, id):
    account = get_object_or_404(Account, id=id)

    context = {
        'account': account,
    }

    return render(request, 'accounts/account-details-page.html', context)


class AccountEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = AccountEditForm
    template_name = 'accounts/account-edit-page.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('account-details')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context

    def get_object(self, queryset=None):
        profile = Profile.objects.get(pk=self.kwargs['id'])
        if profile.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this profile.")
        return profile

    def get_success_url(self):
        return reverse_lazy('account-details', kwargs={'id': self.object.user.id})


def account_delete(request, id):
    account = get_object_or_404(Account, id=id)
    context = {'account': account}

    if account != request.user:
        raise PermissionDenied("You do not have permission to delete this account.")

    if request.method == 'POST':
        account.delete()
        return redirect('index')

    return render(request, 'accounts/close-account-page.html', context)


class AccountReviews(ListView):
    template_name = 'accounts/account-reviews.html'
    paginate_by = 5

    def get_queryset(self):
        review_object = Review.objects.all().filter(user_id=self.kwargs['id'])
        return review_object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = Account.objects.get(id=self.kwargs['id'])
        return context
