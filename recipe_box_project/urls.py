
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import views
from recipes import views as recipe_views




urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('recipes/', include('recipes.urls', namespace='recipes')),    #import from the recipe app
    path('about/', views.about_view),
    path('admin/', admin.site.urls),
    path('', recipe_views.recipe_list_view, name='home'),
]

urlpatterns += staticfiles_urlpatterns()    # works in debug mode
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)