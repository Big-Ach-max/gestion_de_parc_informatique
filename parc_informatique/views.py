from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now

from parc_informatique.forms import AppareilForm, HistoriqueMaintenanceForm, ModificationAppareilForm
from parc_informatique.models import Appareil, HistoriqueMaintenance


def index(request):
    context = {
        "appareils": Appareil.objects.all().order_by("nom"),
    }
    return render(request, "parc_informatique/index.html", context)


def afficher_appareil(request, appareil_id):
    context = {
        "appareil": get_object_or_404(Appareil, pk=appareil_id),
        "local": Appareil.localisation,
    }
    return render(request, "parc_informatique/afficher_appareil.html", context)


def ajouter_appareil(request):
    if request.method == "POST":
        form = AppareilForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("parc_informatique:index")
    else:
        form = AppareilForm()
    context = {"form": form}
    return render(request, "parc_informatique/appareil-form.html", context)


def modifier_appareil(request, appareil_id):
    appareil = Appareil.objects.get(pk=appareil_id)
    if request.method == "POST":
        form = ModificationAppareilForm(request.POST, instance=appareil)

        if form.is_valid():
            form.save()
            return redirect("parc_informatique:index")
    else:
        form = ModificationAppareilForm(instance=appareil)

    return render(request, "parc_informatique/appareil_edit_form.html", {"form": form})


def supprimer_appareil(request, appareil_id):
    appareil = Appareil.objects.get(pk=appareil_id)
    appareil.delete()
    return redirect("parc_informatique:index")



def historique_maintenance(request, appareil_id):
    appareil = get_object_or_404(Appareil, pk=appareil_id)
    maintenances = HistoriqueMaintenance.objects.filter(appareil=appareil).order_by('-date_intervention')
    context = {
        "appareil": appareil,
        "historiquemaintenances": maintenances,
    }
    return render(request, "parc_informatique/historique_maintenance.html", context)


def envoyer_en_maintenance(request, appareil_id):
    appareil = get_object_or_404(Appareil, pk=appareil_id)

    if request.method == "POST":
        form = HistoriqueMaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.appareil = appareil
            maintenance.date_intervention = now().date()
            appareil.etat = "En réparation"
            appareil.save()
            maintenance.save()
            return redirect("parc_informatique:afficher_appareil", appareil_id=appareil.id)
    else:
        form = HistoriqueMaintenanceForm()

    return render(request, "parc_informatique/envoyer_en_maintenance.html", {"form": form, "appareil": appareil})

