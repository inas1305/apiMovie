from django.shortcuts import render
from base64 import b64decode

from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

# Create your views here.

#
# GESTION DES genreS
#
@csrf_exempt
@require_http_methods(["DELETE", "POST", "GET"])
def genre(request, id=None):
    #
    # Gestion de la méthode POST
    #
    if request.method == 'GET':
        if id == None:
            genres = genre.objects.all()
            ns = genreSerializer(genres, many=True)
            return JsonResponse(ns.data, safe=False, status=status.HTTP_200_OK)
        else:
            genres = genre.objects.get(id=id)
            ns = genreSerializer(genres, many=False)
            return JsonResponse(ns.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # réception des données postées par l'utilisateur
        try:
            data = JSONParser().parse(request)
        except ParseError:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        # désérialisations
        genre_serializer = genreSerializer(data=data)

        # Si on a une monument valide, on l'enregistre
        if genre_serializer.is_valid():
            genre_serializer.save()

            return JsonResponse(genre_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(genre_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    #
    # Gestion de la méthode DELETE
    #
    elif request.method == 'DELETE':
        # étant donné que l'on peut ne pas avoir de pk (paramètre facultatif) on fait un try / catch
        try:
            genre_delete = genre.objects.get(pk=id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        genre_delete.delete()

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    #
    # Cas impossible normalement avec le decorator
    #
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
