from django.contrib import admin

# Register your models here.
from .models import KontaktFirma,MitarbeiterUni,Protokoll,Dokument,Firma

admin.site.register(KontaktFirma)
admin.site.register(MitarbeiterUni)
admin.site.register(Protokoll)
admin.site.register(Dokument)
admin.site.register(Firma)
