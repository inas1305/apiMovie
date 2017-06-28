from django.db import models

#GENRES DE FILMS
class Genre(models.Model):
   nom = models.CharField(max_length=100)
   
   def __str__(self):
        
        return self.nom

#FILMS
class Film(models.Model):
   titre = models.CharField(max_length=100)
   genre = models.ForeignKey(Genre)

   def __str__(self):
        
        return self.titre


#Description
class Description(models.Model):
	release_date = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	synopsis = models.CharField(max_length=500)
	film = models.OneToOneField(Film)


#Description
class Comedien(models.Model):
  name = models.CharField(max_length=100)
  actor = models.CharField(max_length=100)
  film = models.ForeignKey(Film, blank=True, null=True)





