from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, FormView
from django.urls import reverse_lazy

from accounts.forms import AccountRegisterForm, AccountLoginForm
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