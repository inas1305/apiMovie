import requests
from monuments.models import *
from monuments.serializers import DescriptionSerializer

def getDescriptionByFilm(filmTitre, filmPk):
    url_params = {"nbpp": "1","key": "572add730149","title": filmTitre}
    query = "https://api.betaseries.com/movies/search"
    req = requests.get(query, params=url_params)
    data = req.json()