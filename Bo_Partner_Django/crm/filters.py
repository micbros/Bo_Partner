import django_filters

from .models import *

class Filter_Bereich(django_filters.FilterSet):
    class Meta:
        model = Firma
        fields = ["name","art","bundesland"]
        filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
         }

