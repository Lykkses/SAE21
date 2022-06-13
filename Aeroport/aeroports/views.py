from django.shortcuts import render, HttpResponseRedirect
from . forms import AeroportsForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = AeroportsForm(request)
        return render(request, "basedonnees/aeroport/formulaire.html", {"form": form})
    else:
        form = AeroportsForm()
        id = ""
        return render(request, "basedonnees/aeroport/formulaire.html", {"form": form})

def traitement(request):
    lform = AeroportsForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indexaeroport/')
    else:
        return render(request, "basedonnees/aeroport/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Aeroports.objects.all())
    return render(request, 'basedonnees/aeroport/index.html', {'liste': liste})


def affiche(request, id):
    aeroport = models.Aeroports.objects.get(pk=id)
    liste = models.Aeroports.objects.filter(avions=id)
    return render(request, 'basedonnees/aeroport/affiche.html', {"aeroport": aeroport, 'liste': liste})


def update(request, id):
    aeroport = models.Aeroports.objects.get(pk=id)
    form = AeroportsForm(aeroport.dico())
    return render(request, 'basedonnees/aeroport/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = AeroportsForm(request.POST)
    if lform.is_valid():
        aeroport = lform.save(commit=False)
        aeroport.id = id
        aeroport.save()
        return HttpResponseRedirect('/aeroports/')
    else:
        return render(request, "aeroport/update.html", {"form": lform, "id": id})


def delete(request, id):
    aeroport = models.Aeroports.objects.get(pk=id)
    aeroport.delete()
    return HttpResponseRedirect('/aeroports/indexaeroport/')
