from django.db import models

class IMDBFilm(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.ImageField(upload_to='')


    def __str__(self):
        return self.title
