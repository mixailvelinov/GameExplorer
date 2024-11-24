from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import Profile

UserModel = get_user_model()


class AccountRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )

    def __init__(self, *args, **kwargs):
        super(AccountRegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your email address'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Confirm your password'})


class AccountLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )

    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your email address'})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your password'})


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture', 'description']

    def __init__(self, *args, **kwargs):
        super(AccountEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your last name'})
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Attach a URL photo...'})
        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'class': 'form-input date-input', 'placeholder': 'Enter your date of birth', 'type': 'date'})
        self.fields['description'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Tell us about yourself...'})

