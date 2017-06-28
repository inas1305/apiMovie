from django.conf.urls import url, include
from rest_framework import routers
from .serializer import GenreViewSet, FilmViewSet, ComedienViewSet, DescriptionViewSet

from . import views

router = routers.DefaultRouter()
router.register(r'v1/genre', GenreViewSet)
router.register(r'v1/film', FilmViewSet)
router.register(r'v1/description', DescriptionViewSet)
router.register(r'v1/comedien', ComedienViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
