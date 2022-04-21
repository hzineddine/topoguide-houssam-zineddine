from django import forms
from .models import Sortie,Itineraire

class SortieForm(forms.ModelForm):
    class Meta:
        model=Sortie
        fields=['date_sortie','duree_reelle','nombre_personne','experience','meteo','difficulte_ressentie']
        