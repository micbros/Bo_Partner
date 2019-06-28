import django_filters

from .models import *

class Filter_Bereich(django_filters.FilterSet):
    suche_bereich = django_filters.ChoiceFilter(choices =Firma.LISTE_BEREICH, field_name='bereich', method='filter_firma_bereich')
    suche_art = django_filters.ChoiceFilter(choices =Firma.LISTE_ART, field_name='art', method='filter_firma_art')
    suche_bundesland =django_filters.ChoiceFilter(choices =Firma.LISTE_BUNDESLAND, field_name='bundesland', method='filter_firma_bundesland')
    suche_befaehigung =django_filters.ChoiceFilter(choices =Firma.LISTE_BEFAEHIGUNG, field_name='befaehigung', method='filter_firma_befaehigung')
  
    def filter_firma_bereich(self, queryset, name, value):
        return queryset.filter(bereich__icontains=value)

    def filter_firma_art(self, queryset, name, value):
        return queryset.filter(art__icontains=value)
    
    def filter_firma_bundesland(self, queryset, name, value):
        return queryset.filter(bundesland__icontains=value)   

    def filter_firma_befaehigung(self, queryset, name, value):
        return queryset.filter(befaehigung__icontains=value)   
      
    
    class Meta:
        model = Firma
        fields = ["name"]

        filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
         }
