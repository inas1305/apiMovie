from rest_framework import serializers, viewsets
from .models import *



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=False)

    class Meta:
        model = Film
        fields = '__all__'


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description

        fields = '__all__'


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer

class ComedienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comedien
        fields = '__all__'

    film = FilmSerializer(many=False)

    #class Meta:
        #model = Comedien
        #fields = '__all__'


class ComedienViewSet(viewsets.ModelViewSet):
    queryset = Comedien.objects.all()
    serializer_class = ComedienSerializer