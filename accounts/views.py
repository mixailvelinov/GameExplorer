from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, CreateView, FormView
from django.urls import reverse_lazy

from accounts.forms import AccountRegisterForm, AccountLoginForm
from accounts.models import Account


# Create your views here.

class AccountRegisterView(CreateView):
    model = Account
    form_class = AccountRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/register-page.html'


class AccountLoginView(LoginView):
    form_class = AccountLoginForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')
