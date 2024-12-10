from django import forms
from common.models import GameSuggestion, Platform, Genre


class GameSuggestionForm(forms.ModelForm):
    class Meta:
        model = GameSuggestion
        fields = ['game_suggestion_name', 'description']


class AddPlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'

    platform_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Platform name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Optional description.."}))


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    genre_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genre name'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': "Optional description.."}))

