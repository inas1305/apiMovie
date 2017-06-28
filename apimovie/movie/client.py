import requests
from .models import *


def getDescriptionByFilm(filmTitre):
    url_params = {"nbpp": "1","key": "572add730149","title": filmTitre}
    query = "https://api.betaseries.com/movies/search"
    req = requests.get(query, params=url_params)    
    data = req.json()
    #Gestion du genre 
    nom_genre = data["movies"][0]["genres"][0]
    genre = Genre.objects.filter(nom=nom_genre).first()
    if genre is None:
        genre = Genre()
        genre.nom = nom_genre
        genre.save()

    # Creer un film
    film = Film()
    id_film = data["movies"][0]["id"]
    film.titre = data["movies"][0]["title"]
    film.genre = genre   
    film.save()

    description = Description()
    description.release_date = data["movies"][0]["release_date"]
    description.director = data["movies"][0]["director"]
    description.synopsis = data["movies"][0]["synopsis"]
    description.film = film
    description.save()

    url_params2 = {"id": id_film, "key": "572add730149"}
    query2 = "https://api.betaseries.com/movies/characters"
    req2 = requests.get(query2, params=url_params2)    
    data2 = req2.json()

    print(data2)

    for c in data2["characters"]:
        comedien = Comedien()
        comedien.name = c["name"]
        comedien.actor = c["actor"]
        comedien.film = film
        comedien.save()

        print(comedien.name)


    #print(data2)
    
    #Parser les datas 
    #Les enregistrer dans la base
    print(description)