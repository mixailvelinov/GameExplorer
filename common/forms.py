from django import forms
from common.models import GameSuggestion


class GameSuggestionForm(forms.ModelForm):
    class Meta:
        model = GameSuggestion
        fields = ['game_suggestion_name', 'description']



