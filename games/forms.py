from django import forms

from games.models import Review


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']

    widgets = {
        'review': forms.Textarea(attrs={'placeholder': 'Write your review here...'}),
    }


