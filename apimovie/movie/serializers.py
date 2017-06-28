from rest_framework import serializers
from movie import models

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        # Vous pouvez ajouter un fields pour filtrer les
        # champs du modèle à sérialiser
        fields = ('nom')

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Post
        fields = ('title', 'text', 'category')