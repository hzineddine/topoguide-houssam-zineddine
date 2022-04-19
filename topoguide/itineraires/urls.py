from django.urls import include, path

from . import views

app_name = 'itineraires'
urlpatterns=[
    path('itineraires/',views.itineraire_list,name='itineraire_list'),
    path('sorties/<int:itineraire_id>/',views.sortie,name='sortie')
]