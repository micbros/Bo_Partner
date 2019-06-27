from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect
from .filters import *


def home (request):
    return render(request, 'bopartner/home.html')

#@login_required
def firmen(request):
    firms = Firma.objects.all()
    return render(request, 'bopartner/firmen.html', {'firms': firms})

@login_required
def neue_firma(request):
    if request.method == "POST":
        form = Neue_firma(request.POST)
        if form.is_valid():
            firma = form.save(commit=False)
            firma.geocode()
            firma.save()
            return redirect('firma_detail', pk=firma.pk)
    else:
        form = Neue_firma()
    return render(request, 'bopartner/neue_firma.html', {'form': form})


def edit_firma(request, pk):
    firma = get_object_or_404(Firma, pk=pk)
    form = Neue_firma(request.POST or None, instance=firma)
    if form.is_valid():
        form.save()
        return redirect('firma_detail', pk=firma.pk)
    return render(request, 'bopartner/edit_firma.html', {'form': form})

#@login_required
def firma_detail(request, pk):
    firma = get_object_or_404(Firma, pk=pk)
    kontakte = KontaktFirma.objects.all()
    return render(request, 'bopartner/firma_detail.html', {'firma': firma, 'kontakte':kontakte})

@login_required
def neuer_kontakt(request):
    if request.method == "POST":
        form = Neuer_kontakt(request.POST)
        if form.is_valid():
            kontakt = form.save(commit=False)
            kontakt.save()
            form.save_m2m()
            return redirect('kontakt_detail', pk = kontakt.pk)
    else:
        form = Neuer_kontakt()
    return render(request, 'bopartner/neuer_kontakt.html', {'form': form})

def edit_kontakt(request, pk):
    kontakt = get_object_or_404(KontaktFirma, pk=pk)
    form = Neuer_kontakt(request.POST or None, instance=kontakt)
    if form.is_valid():
        form.save()
        return redirect('kontakt_detail', pk=kontakt.pk)
    return render(request, 'bopartner/edit_kontakt.html', {'form': form})


def kontakt_detail(request, pk):
    kontakt = get_object_or_404(KontaktFirma, pk=pk)
    return render(request, 'bopartner/kontakt_detail.html', {'kontakt':kontakt})

@login_required
def eigene_kontakte(request):
    eigene_kontakte = KontaktFirma.objects.filter(hsbo_mitarbeiter=request.user)
    return render(request, 'bopartner/eigene_kontakte.html', {'eigene_kontakte': eigene_kontakte})

#@login_required
def firmen_kartenuebersicht(request):
    firmen = Firma.objects.all()
    return render(request, 'bopartner/firmen_kartenuebersicht.html', {'firmen': firmen})

def firmen_gefiltert(request):
    firmen_liste = Firma.objects.all().order_by('name')
    firmen_filter = Filter_Bereich(request.GET,queryset=firmen_liste)
    return render(request, 'bopartner/firmen_gefiltert.html', {'filter': firmen_filter})

def firmen_kartenuebersicht_gefiltert(request):
    firmen_liste = Firma.objects.all()
    firmen_filter = Filter_Bereich(request.GET,queryset=firmen_liste)
    return render(request, 'bopartner/firmen_kartenuebersicht_gefiltert.html', {'filter': firmen_filter})
