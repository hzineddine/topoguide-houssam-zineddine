from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Itineraire,Sortie
from django.contrib.auth.decorators import login_required
@login_required
def itineraire_list(request):
    list_itineraire=Itineraire.objects.order_by('id')
    
    return render(request,'itineraires/itineraires.html',{'list_itineraire' : list_itineraire})
def sortie(request,itineraire_id):
    list_sortie = Sortie.objects.filter(itineraire_id=itineraire_id)
    
    
    return render(request,'itineraires/sortie.html',{'list_sortie': list_sortie} )

def detail_sortie(request,sortie_id):
    sortie=get_object_or_404(Sortie,id=sortie_id)
    return render(request, 'itineraires/detail_sortie.html',{'sortie':sortie})
    
# Create your views here.
