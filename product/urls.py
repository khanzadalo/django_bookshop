from django.urls import path
from . import views

urlpatterns = [
    path('kids_clothes/', views.KidsClothesList.as_view(), name='kids_clothes_list'),
    path('womens_clothes/', views.WomensClothesList.as_view(), name='womens_clothes_list'),
    path('mens_clothes/', views.MensClothesList.as_view(), name='mens_clothes_list'),
    path('pensioners_clothes/', views.PensionersClothesList.as_view(), name='pensioners_clothes_list'),
]