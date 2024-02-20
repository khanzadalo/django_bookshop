from django import forms
from . import parser_imdb, models

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        'imdb.com', 'imdb.com',
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type',]


    def parser_data(self):
        if self.data['media_type'] == 'imdb.com':
            film_parser_imdb = parser_imdb.parser()
            for film in film_parser_imdb:
                models.IMDBFilm.objects.create(**film)



