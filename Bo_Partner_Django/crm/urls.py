from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eigene_kontakte', views.eigene_kontakte, name='eigene_kontakte'),
    path('firmen/neue_Firma', views.neue_firma, name='neue_firma'),
    path('firmen/firma_detail/<int:pk>', views.firma_detail, name='firma_detail'),
    path('firmen/neuer_kontakt', views.neuer_kontakt, name='neuer_kontakt'),
    path('firmen/kontakt_detail/<int:pk>', views.kontakt_detail, name='kontakt_detail'),
    path('firmen_kartenuebersicht', views.firmen_kartenuebersicht, name='firmen_kartenuebersicht'),
    url(r'^firmen_gefiltert/$', views.firmen_gefiltert, name='firmen_gefiltert'),
    url(r'^firmen_kartenuebersicht_gefiltert/$', views.firmen_kartenuebersicht_gefiltert, name='firmen_kartenuebersicht_gefiltert'),
]
