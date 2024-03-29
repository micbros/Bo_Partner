from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
import geocoder


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
    
    LISTE_BEFAEHIGUNG = (
            ('Bachelorarbeit', 'Bachelorarbeit'),
            ('Masterarbeit', 'Masterarbeit'),
            ('Praktikum', 'Praktikum'),
            ('Exkursion', 'Exkursion')
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
    befaehigung =  MultiSelectField(max_length=200, choices=LISTE_BEFAEHIGUNG, null=True, blank=True)

    def __str__(self):
        return  str(self.name) + " Primarykey: "+ str(self.pk)

    def geocode(self):
        hsnrzus = self.hausnummerzusatz if self.hausnummerzusatz else ""
        address = self.strasse + " " + str(self.hausnummer) + hsnrzus + ", " + self.ort
        geocode_result = geocoder.osm(address)

        self.xKoordinate = geocode_result.latlng[0]
        self.yKoordinate = geocode_result.latlng[1]


    class Meta:
        verbose_name_plural = "Firmen"


class KontaktFirma(models.Model):

    #id_kontakt = models.
    vorname = models.CharField(max_length=50, blank=False) #max_length = required
    nachname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    telefon2 = models.CharField(max_length=30, blank=True, null=True)
    freie_beschreibung = models.TextField(null=True, blank=True)
    
    firma = models.ForeignKey(Firma,on_delete=models.SET_NULL, null=True, blank=False)
    hsbo_mitarbeiter = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=False)

    def __str__(self):
        return str(self.nachname)+" "+str(self.vorname) + " Primarykey: "+ str(self.pk)

    class Meta:
        verbose_name_plural = "Kontakt Firmen"
#---------------------------------------------------------    

class Protokoll(models.Model):
    #id_protokoll = models.
    datum = models.DateTimeField(blank=False)
    verfasser = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    
    kontaktfirma = models.ForeignKey(KontaktFirma, on_delete=models.CASCADE, default=-1)


    class Meta:
        verbose_name_plural = "Protokolle"

class Dokument(models.Model):
    #id_dokument = models.
    titel = models.CharField(max_length=100, blank=False)
    datei = models.FileField(blank=False)
    hochlader = models.CharField(max_length=100, blank=False)
    freie_beschreibung = models.TextField(null=True)
    
    firma = models.ForeignKey(Firma,on_delete=models.SET_NULL, null=True, blank=True)
    kontaktfirma = models.ForeignKey(KontaktFirma, on_delete=models.CASCADE, default=-1)


    class Meta:
        verbose_name_plural = "Dokumente"