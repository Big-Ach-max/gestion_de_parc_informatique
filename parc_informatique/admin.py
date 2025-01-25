from django.contrib import admin

from django.contrib import admin
from .models import Local, Utilisateur, Appareil, HistoriqueMaintenance

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'etage', 'batiment')
    list_filter = ['etage']
    search_fields = ['nom']
    list_per_page = 5 

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone', 'poste')
    list_filter = ['nom']
    search_fields = ['nom']
    list_per_page = 5

@admin.register(Appareil)
class AppareilAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'marque', 'modele', 'numero_serie', 'etat', 'date_acquisition', 'localisation', 'utilisateur')
    list_filter = ['marque']
    search_fields = ['modele']
    list_per_page = 5


@admin.register(HistoriqueMaintenance)
class HistoriqueMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('appareil', 'date_intervention', 'description', 'technicien', 'statut')
    list_filter = ['date_intervention']
    search_fields = ['appareil']
    list_per_page = 5


# admin.site.register(Local)
# admin.site.register(Utilisateur)
# admin.site.register(Appareil)
# admin.site.register(HistoriqueMaintenance)

