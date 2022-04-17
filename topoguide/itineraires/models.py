from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Niveau(models.Model):
    niveau=models.IntegerField('Niveau')
    def __str__(self):
        return str(self.niveau) 
class Itineraire(models.Model):
    titre = models.CharField(max_length=200)
    point_depart=models.CharField(max_length=200)
    description=models.TextField()
    altitude_depart=models.IntegerField('Altitude (m) ')
    altitude_max=models.IntegerField('Altitude max (m) ')
    altitude_min=models.IntegerField('Altitude min (m) ')
    denivele_positif=models.IntegerField( 'Dénivelé positif (m) ')
    denivele_negatif = models.IntegerField('Dénivelé négatif (m) ')
    duree_estimee=models.FloatField('Durée (h) ')
    difficulte_estimee=models.ForeignKey('Niveau',on_delete=models.CASCADE)
    def __str__(self):
        return self.titre
class Experience(models.Model):
    choix=models.CharField(max_length=100)
    def __str__(self):
        return self.choix
    
class Meteo(models.Model):
    choix=models.CharField(max_length=100)
    def __str__(self):
        return self.choix
   
class Sortie(models.Model):
    utilisateur=models.ForeignKey(User,on_delete=models.CASCADE)
    itineraire = models.ForeignKey('Itineraire',on_delete=models.CASCADE)
    date_sortie=models.DateField('Date de sortie')
    duree_reelle=models.FloatField('Durée réelle')
    nombre_personne=models.IntegerField('Nombres de personnnes')
    experience=models.ForeignKey('Experience',on_delete=models.CASCADE)
    meteo=models.ForeignKey('Meteo',on_delete=models.CASCADE)
    difficulte_ressentie=models.ForeignKey('Niveau',on_delete=models.CASCADE)
    
    
    
    
    
        
# Create your models here.
