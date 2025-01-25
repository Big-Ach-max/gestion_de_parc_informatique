from django.urls import path
from . import views

app_name = 'parc_informatique'


urlpatterns = [
    path("", views.index, name='index'), # Page d'acceuil
    path("appareils/<int:appareil_id>/", views.afficher_appareil, name='afficher_appareil'), # Liste des appareils
    path("ajouter-appareil/", views.ajouter_appareil, name="ajouter_appareil"),
    path("appareils/<int:appareil_id>/modifier/", views.modifier_appareil, name="modifier_appareil"),
    path("appareils/<int:appareil_id>/supprimer/", views.supprimer_appareil, name="supprimer_appareil"),
    path("appareils/<int:appareil_id>/maintenance/", views.historique_maintenance, name='historique_maintenance'),
    path("appareils/<int:appareil_id>/evoyer_en_maintenance/", views.envoyer_en_maintenance, name="envoyer_en_maintenance"),
]
