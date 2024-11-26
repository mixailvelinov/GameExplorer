from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView, FormView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from accounts.forms import AccountRegisterForm, AccountLoginForm, AccountEditForm
from accounts.models import Account, Profile


# Create your views here.

class AccountRegisterView(CreateView):
    model = Account
    form_class = AccountRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/register-page.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        login(self.request, self.object)
        return response


class AccountLoginView(LoginView):
    form_class = AccountLoginForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class AccountLogoutView(LogoutView):
    pass


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


