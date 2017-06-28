from django.conf.urls import url

from . import views

urlpatterns = [

    # Genres routes
    url(r'^genre$', views.genre, name='genre'),
    url(r'^genre/(?P<id>\d+)$', views.genre, name='genre_id'),

]
