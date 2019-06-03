from django import forms
from django.shortcuts import render, get_object_or_404

from .models import *





class Neue_firma(forms.ModelForm):
    class Meta:
        model = Firma
        fields = ('name', 'freie_beschreibung', 'strasse', 'hausnummer', 'hausnummerzusatz',
                  'plz', 'ort', 'bundesland', 'land', 'xKoordinate', 'yKoordinate', 'bereich')

class Neuer_kontakt(forms.ModelForm):
    class Meta:
        model = KontaktFirma
        fields = ('vorname','nachname','email','freie_beschreibung', 'firma')



        #test kommentar
