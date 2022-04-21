from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Itineraire,Sortie
from django.contrib.auth.decorators import login_required
from .forms import SortieForm
@login_required
def itineraire_list(request):
    list_itineraire=Itineraire.objects.order_by('id')
    
    return render(request,'itineraires/itineraires.html',{'list_itineraire' : list_itineraire})
def sortie(request,itineraire_id):
    current_user=request.user
    list_sortie = Sortie.objects.filter(itineraire_id=itineraire_id)
    
    
    return render(request,'itineraires/sortie.html',{'list_sortie': list_sortie} )

def detail_sortie(request,sortie_id):
    sortie=get_object_or_404(Sortie,id=sortie_id)
    return render(request, 'itineraires/detail_sortie.html',{'sortie':sortie})
def nouvelle_sortie(request):
    
     
    if request.method=="POST":
        sortie_form=SortieForm(request.POST)
        if sortie_form.is_valid():
            form=sortie_form.save(commit=False)
            form.utilisateur=request.user
            form.save()
            return redirect('/sortie/'+str(Sortie.objects.latest('id').id))



    else :
        sortie_form=SortieForm()
    return render(request,'itineraires/nouvelle_sortie.html',{'sortie_form':sortie_form})

def modifier_sortie(request,sortie_id):
    sortie=get_object_or_404(Sortie, pk=sortie_id)
    if request.method == "POST":
        sortie_form = SortieForm(request.POST,instance=sortie)
        if sortie_form.is_valid():
            sortie=sortie_form.save(commit=False)
            sortie.utilisateur=request.user
            sortie.save()
            return redirect('../../sortie/'+str(sortie_id),pk=sortie_id)     
    else :
        sortie_form=SortieForm(instance=sortie)
    return render(request,'itineraires/modifier_sortie.html',{'sortie_form' : sortie_form})  
    
# Create your views here.
