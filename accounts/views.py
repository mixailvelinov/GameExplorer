from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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
    account = request.user

    context = {
        'account': account,
    }

    return render(request, 'accounts/account-details-page.html', context)


class AccountEditView(UpdateView):
    model = Profile
    form_class = AccountEditForm
    template_name = 'accounts/account-edit-page.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('account-details')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = self.request.user
        return context

    def get_success_url(self):
        return reverse_lazy('account-details', kwargs={'id': self.object.user.id})


def account_delete(request, id):
    account = request.user
    context = {'account': account}

    if request.method == 'POST':
        account.review_set.all().delete()
        # Delete the user/account
        account.delete()
        return redirect('index')

    return render(request, 'accounts/close-account-page.html', context)


