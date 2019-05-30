from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.

class Firma(models.Model):
    
    LISTE_BUNDESLAND = (
            ('BB', 'Brandenburg'),
            ('BE', 'Berlin'),
            ('BW', 'Baden-Wuerttemberg'),
            ('BY', 'Bayern'),
            ('HB', 'Bremen'),
            ('HE', 'Hessen'),
            ('HH', 'Hamburg'),
            ('MV', 'Mecklenburg-Vorpommern'),
            ('NI', 'Niedersachsen'),
            ('NW', 'Nordrhein-Westfalen'),
            ('RP', 'Rheinland-Pfalz'),
            ('SH', 'Schleswig-Holstein'),
            ('SL', 'Saarland'),
            ('SN', 'Sachsen'),
            ('ST', 'Sachsen-Anhalt'),
            ('TH', 'Thueringen'),
    )
    
    LISTE_ART = (
            ('Behoerde','Behoerde'),
            ('Firma','Firma'),
            ('Institut', 'Institut'),
            ('Verband', 'Verband')
    )
    
    LISTE_BEREICH = (
            ('Agrarwirtschaft','Agrarwirtschaft'),
            ('CAD','CAD'),
            ('Geo- und Landschaftsökologie','Geo- & Landschaftsökologie'),
            ('Geodäse und Vermessung','Geodäse und Vermessung'),
            ('Geodaten','Geodaten'),
            ('Geographie','Geographie'),
            ('Geoinformatik','Geoinformatik'),
            ('Geologie','Geologie'),
            ('Geomarketing','Geomarketing'),
            ('Geophysik','Geophysik'),
            ('Geowissenschaften','Geowissenschaften'),
            ('GIS','GIS'),
            ('GIS-Applikation','GIS-Applikation'),
            ('Hydrologie und Wasserbau','Hydrologie und Wasserbau'),
            ('Kartographie und Visualisierung','Kartographie und Visualisierung'),
            ('Meteorologie','Meteorologie'),
            ('Navigation und Telematik','Navigation und Telematik'),
            ('Photogrammetrie','Photogrammetrie'),
            ('Planung','Planung'),
            ('Raumordnung','Raumordnung'),
            ('Software-Entwicklung','Software-Entwicklung'),
            ('Umwelt- und Naturschutz','Umwelt- und Naturschutz'),
            ('Verkehr','Verkehr'),
            ('Vermessung','Vermessung')
    )
    
    #id_firma = models.
    name = models.CharField(max_length=100, blank=False)
    art = models.CharField(max_length=50, choices=LISTE_ART, null=True)
    freie_beschreibung = models.TextField(null=True, blank=True)
    strasse = models.CharField(max_length=100, blank=False)
    hausnummer = models.IntegerField(blank=False)
    hausnummerzusatz = models.CharField(max_length=10, null=True, blank=True)
    plz = models.IntegerField(blank=False)
    ort = models.CharField(max_length=50, blank=False)
    bundesland = models.CharField(max_length=2, blank=False, choices=LISTE_BUNDESLAND)
    land = models.CharField(max_length=50, blank=False)
    xKoordinate = models.FloatField(null=True, blank=True)
    yKoordinate = models.FloatField(null=True, blank=True)
    bereich = MultiSelectField(max_length=200, choices=LISTE_BEREICH, null=True, blank=True)

    def __str__(self):
        return  str(self.name) + " Primarykey: "+ str(self.pk)
  
class KontaktFirma(models.Model):
    #id_kontakt = models.
    vorname = models.CharField(max_length=50, blank=False) #max_length = required
    nachname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(null=True)
    freie_beschreibung = models.TextField(null=True, blank=True)
    
    firma = models.ForeignKey(Firma,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.nachname)+" "+str(self.vorname) + " Primarykey: "+ str(self.pk)
#---------------------------------------------------------    
class MitarbeiterUni(models.Model):
    #id_mitarbeiter = models.
    vorname = models.CharField(max_length=50, blank=False) #max_length = required
    nachname = models.CharField(max_length=50, blank=False)
    status = models.CharField(max_length=50, blank=True)
    
class Protokoll(models.Model):
    #id_protokoll = models.
    datum = models.DateTimeField(blank=False)
    verfasser = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    
    kontaktfirma = models.ForeignKey(KontaktFirma, on_delete=models.CASCADE, default=-1)
    
class Dokument(models.Model):
    #id_dokument = models.
    titel = models.CharField(max_length=100, blank=False)
    datei = models.FileField(blank=False)
    hochlader = models.CharField(max_length=100, blank=False)
    freie_beschreibung = models.TextField(null=True)
    
    firma = models.ForeignKey(Firma,on_delete=models.SET_NULL, null=True, blank=True)
    kontaktfirma = models.ForeignKey(KontaktFirma, on_delete=models.CASCADE, default=-1)