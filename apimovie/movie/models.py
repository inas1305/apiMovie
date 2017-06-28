from django.db import models

#GENRES DE FILMS
class Genre(models.Model):
   nom = models.CharField(max_length=100)
   
   def __str__(self):
        
        return self.nom

#FILMS
class Film(models.Model):
   titre = models.CharField(max_length=100)
   date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
   genre = models.ForeignKey('Genre')

   def __str__(self):
        
        return self.titre


