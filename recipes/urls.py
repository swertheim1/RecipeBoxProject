
from django.urls import path, re_path
from . import views


app_name='recipes'
urlpatterns = [
    path('', views.recipe_list_view, name='list'),
    path('search/', views.recipe_search_view, name='search'),
    path('create/', views.recipe_create_view, name='create'),
    path('<slug:slug>/', views.recipe_detail_view, name='detail'),
]