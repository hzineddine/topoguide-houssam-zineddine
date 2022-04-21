from django.urls import include, path

from . import views

app_name = 'itineraires'
urlpatterns=[
    path('itineraires/',views.itineraire_list,name='itineraire_list'),
    path('itineraires/sorties/<int:itineraire_id>/',views.sortie,name='sorties'),
    path('itineraires/sortie/<int:sortie_id>/',views.detail_sortie,name='detail_sortie'),
    path('itineraires/nouvelle_sortie/<int:itineraire_id>',views.nouvelle_sortie,name='nouvelle_sortie'),
    path('itineraires/modifier_sortie/<int:sortie_id>/',views.modifier_sortie,name='modifier_sortie')
]