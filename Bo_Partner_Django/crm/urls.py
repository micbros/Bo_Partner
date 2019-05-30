from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.firmen, name='firmen'),
    path('firmen', views.firmen, name='firmen'),
    path('firmen/neue_Firma', views.neue_firma, name='neue_firma'),
    path('firmen/firma_detail/<int:pk>', views.firma_detail, name='firma_detail'),
    path('firmen/neuer_kontakt', views.neuer_kontakt, name='neuer_kontakt'),

]
