from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150, verbose_name='Tag of cloth')

    def __str__(self):
        return self.name


class ProductCloth(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name of cloth')
    image = models.ImageField(upload_to='', null=True, verbose_name='Image of cloth')
    description = models.TextField(blank=True, verbose_name='Description of cloth')
    price = models.PositiveIntegerField(verbose_name='Price of cloth')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title