from django import forms
from django.core.exceptions import ValidationError

from common.models import GameSuggestion, Platform, Genre


class GameSuggestionForm(forms.ModelForm):
    class Meta:
        model = GameSuggestion
        fields = ['game_suggestion_name', 'description']


class AddPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'

    def clean_platform_name(self):
        platform_name = self.cleaned_data.get('platform_name')
        if Platform.objects.filter(platform_name=platform_name).exists():
            raise ValidationError(f"The platform '{platform_name}' already exists.")

        return platform_name

    platform_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Platform name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Optional description.."}))


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    genre_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genre name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Optional description.."}))

    def clean_genre_name(self):
        genre_name = self.cleaned_data.get('genre_name')
        if Genre.objects.filter(genre_name=genre_name).exists():
            raise ValidationError(f"The genre '{genre_name}' already exists.")

        return genre_name
