# Bo_Partner

Ein Customer-Relationshipmodell der Hochschule Bochum. Mit dieser Django-Applikation ist es der Hochschule Bochum möglich, Partner-Firmen und deren Kontakte zu verwalten. 
<br>
Das Projekt wurde im Rahmen des Bachelor-Studienganges "Geoinformatik 6. Semester 2019" der Hochschule Bochum durchgeführt. Umgesetzt wurde dies mit dem Webframework Django.
<br>
### Funktionen
<ul>
  <li>Filterung der Partner nach verschiedenen Attributen</li>
  <li>Anzeige der gefilterten Partner in einer Karte</li>
</ul>
### Funktionen-Login erforderlich
<ul>
  <li>Anlegen von Partner Firmen</li>
  <li>Anlegen von Kontakten</li>
  <li>Anzeigen eigener Kontakte</li>
  <li>Änderung von Partner Firmen und Kontakten</li>
</ul>

### Starten des Servers
<ul>
  <li>Bo_Partner/Bo_Partner_Django/manage.py --> Skript zur Steuerung des Servers</li>
  <li>python manage.py migrate --> stellt Veränderungen der allgemeinen Modelle fest (User usw.)</li>
  <li>python manage.py makemigrations --> übernimmt die Veränderungen in die Datenbank</li>
  <li>python manage.py migrate crm --> stellt Veränderungen der Modelle fest (Kontakt, Partner, usw.)</li>
  <li>python manage.py makemigrations crm --> übernimmt die Veränderungen in die Datenbank</li>
  <li>python manage.py createsuperuser --> legt Super-User an </li>
  <li>python manage.py runserver --> startet den Server  http://127.0.0.1:8000/  </li>
</ul>

### Admin Seite
http://127.0.0.1:8000/admin/ <br><br>

Mittels dieser Seite, lassen sich umfangreiche Administrationen durchführen. Kontakte und Firmen lassen sich ändern und anlegen. Zudem gibt es eine umfangreiche Möglichkeit Benutzer und Rechte zu verwalten.
