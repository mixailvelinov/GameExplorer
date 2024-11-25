from django import forms

from games.models import Review


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']


