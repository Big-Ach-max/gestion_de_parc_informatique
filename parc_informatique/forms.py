from django import forms
from parc_informatique.models import Appareil, HistoriqueMaintenance, Local, Utilisateur

class AppareilForm(forms.ModelForm):
    ETAT_CHOICES = [
        ("Disponible", "Disponible"),
        ("En réparation", "En réparation"),
        ("Obsolète", "Obsolète"),
    ]
    TYPE_CHOICES = [
        ("Desktop", "Desktop"),
        ("Laptop", "Laptop"),
        ("Périphérique", "Périphérique"),
    ]

    class Meta:
        model = Appareil
        fields = [
            'nom',
            'type',
            'marque',
            'modele',
            'numero_serie',
            'etat',
            'date_acquisition',
            'localisation',
            'utilisateur',
        ]
        labels = {
            'nom': 'Nom',
            'type': 'Type',
            'marque': 'Marque',
            'modele': 'Modèle',
            'numero_serie': 'Numéro de série',
            'etat': 'Etat',
            'date_acquisition': 'Date',
            'localisation': 'Localisation',
            'utilisateur': 'Utilisateur',
        }
        widgets = {
            "date_acquisition": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }


class ModificationAppareilForm(forms.ModelForm):
    ETAT_CHOICES = [
        ("Disponible", "Disponible"),
        ("En réparation", "En réparation"),
        ("Obsolète", "Obsolète"),
    ]
    class Meta:
        model = Appareil
        fields = ['etat']
        label = {'etat': 'Etat'}
    

class HistoriqueMaintenanceForm(forms.ModelForm):
    
    class Meta:
        model = HistoriqueMaintenance
        fields = ["date_intervention","description", "technicien", "statut"]
        labels = {
            "date_intervention": "Date d'intervention",
            "description": "Description du problème ou de la maintenance",
            "technicien": "Technicien", 
            "statut": "Statut"
        }
        
        widgets = {
            "date_intervention": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Expliquez pourquoi l'appareil nécessite une maintenance."}
            ),
            "technicien": forms.TextInput(attrs={"class": "form-control"}),
            "statut": forms.Select(attrs={"class": "form-control"}),
        }