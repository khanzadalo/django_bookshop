from django.urls import path
from . import views

urlpatterns = [
    path('start_parser/', views.ParserFormView.as_view(), name='start_parser')
]