from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect

@login_required
def firmen(request):
    firms = Firma.objects.all()
    return render(request, 'bopartner/firmen.html', {'firms': firms})

@login_required
def neue_firma(request):
    if request.method == "POST":
        form = Neue_firma(request.POST)
        if form.is_valid():
            firma = form.save(commit=False)
            firma.save()
            return redirect('firma_detail', pk=firma.pk)
    else:
        form = Neue_firma()
    return render(request, 'bopartner/neue_firma.html', {'form': form})


@login_required
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
            return redirect('firmen')
    else:
        form = Neuer_kontakt()
    return render(request, 'bopartner/neuer_kontakt.html', {'form': form})

@login_required
def kontakt_detail(request, pk):
    kontakt = get_object_or_404(Firma, pk=pk)
    return render(request, 'bopartner/firma_detail.html', {'kontakt':kontakt})