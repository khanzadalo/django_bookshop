from django.urls import path
from . import views


urlpatterns = [
    path('', views.TVShowListView.as_view(), name='tv_shows_list'),
    path('tv_shows_list/<int:id>/', views.TVShowDetailView.as_view(), name='tv_show_detail'),
    path('tv_shows_list/<int:id>/delete', views.DeleteTVShowView.as_view(), name='delete_tvshow'),
    path('tv_shows_list/<int:id>/update', views.EditTVShowView.as_view(), name='update_tvshow'),
    path('create_tvshow/', views.TVShowCreateView.as_view(), name='create_tvshow'),
    path('add_review/', views.add_review_view, name='add_review'),
    path('search/', views.SearchTVShowView.as_view(), name='search'),

]