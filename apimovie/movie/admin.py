from django.contrib import admin
from .models import *
from django.shortcuts import render
from .client import getDescriptionByFilm



def get_info(request, *args, **kwargs):
	if request.method == "POST":
		getDescriptionByFilm("Terminator")
	
	return render(request, 'admin/pull.html')

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Description)
admin.site.register(Comedien)

#enregistrer la route et l'afficher sur l'admin
admin.site.register_view('get_info', view=get_info, visible=True)
