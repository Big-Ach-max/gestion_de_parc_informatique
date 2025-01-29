from django.db import models

from django.utils import timezone


class Local(models.Model):
    nom = models.CharField(max_length=100)
    etage = models.CharField(max_length=50, blank=True)
    batiment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.batiment}, étage {self.etage})"


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    poste = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Appareil(models.Model):
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

    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=100, blank=True)
    modele = models.CharField(max_length=100, blank=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    etat = models.CharField(max_length=50, choices=ETAT_CHOICES, default="Disponible")
    date_acquisition = models.DateField(blank=True, null=True)
    localisation = models.ForeignKey(
        Local, on_delete=models.SET_NULL, null=True, related_name="appareils"
    )
    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appareils",
    )

    def __str__(self):
        return f"{self.nom} ({self.marque} {self.modele})"


class HistoriqueMaintenance(models.Model):
    STATUT_CHOICES = [
        ("Réparé", "Réparé"),
        ("Non réparé", "Non réparé"),
    ]

    appareil = models.ForeignKey(
        Appareil, on_delete=models.CASCADE, related_name="maintenances"
    )
    date_intervention = models.DateField()
    description = models.TextField()
    technicien = models.CharField(max_length=100)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default="Réparé")

    def __str__(self):
        return f"Maintenance de {self.appareil.nom} le {self.date_intervention}"
