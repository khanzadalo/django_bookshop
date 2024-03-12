from django.views import generic
from django.shortcuts import get_object_or_404

from product import models


class KidsClothesList(generic.ListView):
    template_name = 'products/kids_clothes_list.html'
    context_object_name = 'kids_clothes'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#kids clothes").order_by("-id")


class WomensClothesList(generic.ListView):
    template_name = 'products/womens_clothes_list.html'
    context_object_name = 'womens_clothes'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#womens clothes").order_by("-id")


class MensClothesList(generic.ListView):
    template_name = 'products/mens_clothes_list.html'
    context_object_name = 'mens_clothes'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#mens clothes").order_by("-id")


class PensionersClothesList(generic.ListView):
    template_name = 'products/pensioners_clothes_list.html'
    context_object_name = 'pensioners_clothes'
    model = models.ProductCloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="#pensioners clothes").order_by("-id")