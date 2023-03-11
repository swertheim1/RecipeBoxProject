
from django.urls import path, re_path
from . import views


app_name='recipes'
urlpatterns = [
    path('', views.recipe_list_view, name='list'),
    # re_path(r'^(?P<slug>[\w-]+/$)', views.recipe_detail_view, name='detail'),
    path('<slug:slug>/', views.recipe_detail_view, name='detail'),
    

]