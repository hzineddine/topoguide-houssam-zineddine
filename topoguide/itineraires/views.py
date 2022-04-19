from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Itineraire,Sortie
from django.contrib.auth.decorators import login_required
@login_required
def itineraire_list(request):
    list_itineraire=Itineraire.objects.order_by('id')
    
    return render(request,'itineraires/itineraires.html',{'list_itineraire' : list_itineraire})
    
# Create your views here.
