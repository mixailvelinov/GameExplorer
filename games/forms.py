from django import forms

from games.models import Review, Game


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']

    widgets = {
        'review': forms.Textarea(attrs={'placeholder': 'Write your review here...'}),
    }


#admin only forms
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('slug', )

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Game name'}))
    release_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Release date (YYYY-MM-DD)'}))
    developer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Game developer'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "What's the game about? Share a bit without spoiling the whole story..."}))
    game_cover = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Game cover URL'}))


class DeleteGame(GameForm):
    def __init__(self, *args, **kwargs):
        super(DeleteGame, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
