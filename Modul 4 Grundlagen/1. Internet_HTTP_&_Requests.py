### -------------------- Backend Modul 4 ----------------------------- ###

## ------------ Internet, HTTP und Requests --------------------##

# --------------   01 - Was ist das Internet ---------------- #

# Das Intenet ist dafür da um mehrere Computzer mit einander zu verbinden.
# Jedes Gerät das mit dem Intenet verbunden ist hat eine Ip Adresse, stell es dir wie ein Telefonbuch vor.
# Man kann mit der adresse eines Computers Datenaustauschen. 
# Domains werden durch einen DNS Server des Provides zur Ip aufgelöst.
# Domains lasen sich leichter merken als lange ip Adressen. 

# Jede anfrage geht normalerweise erst an den Provider der schaut in seiner DNS list nach und verbindet uns dann über die IP.




# --------------   02 - Frontend vs. Backend ---------------- #

# Was ist der Unterschied zwischen Frontend & Backend? 

# Forontend : 
    # Die software die sich auf dem Endgerät des Nutzersbefindet nent man Frontend. 

# Backend : 
    # Was im Hintergrund passiert Datenbanken, Server, Datenbereitstellen usw ist das Backend.




# --------------   03 - Was ist eine API? ---------------- #

# Api =  Application Programming Interface

# Api was ist das ? 
    # Eine Api ist eine Schnitstelle, wenn man mit einem Server Kommuniziert will.
    # Sie dient dem Austausch von daten z.b. vom Backend and das Frontend.
    # Das Frontend die Application auf dem Endgerät, fragt z.b. aktuelle daten an, diese geschit über die Api schnitstelle.
    # Es wird eine anfrage über die Schnitstelle mit der erforderlichen berechtiegung angefragt, das Backend liefert diese dann zurück. 
    # Diese verarbeitet das Forntend und zeigt die informationen an. 

# Rest Api, was ist das ? 
    # Rest steht für : Representational
    #                  State
    #                  Transfer
    
    # Das ganze ist ein Standard für Programmier Schnitstellen.

    # Aufbai eine Api URL:
        # pokeapi.co/api/v2/pokemon/?limit=5
            # /api : dadurch greifen man auf die Api zu#
            # /v2  : Es gibt meist verschiedene Versionen, hier greifen wir auf 
            #        version 2 zu, Version 1 bleibt aber dennoch aktiv. Dies 
            #        hat den vorteil, das auch ältere Projekte die V1 verwenden 
            #        weiterhin funktionieren
            # /pokemon : Hier sagen wir auf welche Resurce ich über die Api 
            #            zugreifen möchte. Diese wird uns als JSNON zurück 
            #            gegeben.
            # /?linit=5 : Dies sind Querey Paramteter und ermöglichen es limits 
            #             oder filter einzusetzen um das gewünschte Ergebnis 
            #             abzufragen. Dadurch kann man die anfrage 
            #             geschwindigkeit beeinflussen z.b. 
        # Beispiel: 
            # /customers : Fragt alle kunden der APi ab 
            # /customers/{custimerId} : fragt die infos zu einem bestimten 
            #                           KundenId ab
            # /customers/{custimerId}/accounts/{accountId} 
            # /customers/{custimerId}/accounts/?city=munich&age>18 :
            #   # Nur die accounts eines nutzers aus München anzeigen der >18 is

# Wie eine Rest Api aufgebaut ist, entnimmt man der Doku



# --------------    04 - Was ist HTTP? ---------------- #

# Was ist HTTP & HTTPS
    # Das ist das Protokoll, mmit dem man meistens mit dem Internet kommunizierst.

    # Über diese Protokoll wird beispilesweise HTML, Css, Javascript, Json usw code transferiert aber auch alle anderen daten 

    # HTTP ist auf der 7 Schicht des ISO OSI Models


    # HTTP steht für : Hypertext = 
    #                  Transfer
    #                  Protcol

    # HTTPS steht für : Hypertext   = 
        #               Transfer
        #               Protcol
        #               Secure

    # Der Client baut eine Verbindung mit einem Server auf, über einen HTTP Request. 
    # Der Server Empfängt diese anfrage und verarbeitet sie ung gibt dann eine Response (HTTP Message) an den Client zurück.

    # Weitere Protokolle sind z.b. 
        # FTP / SFTP = File transfer Protocol & SSH File Transfer Protocol

        # WS  / WSS  = Websocket & Der getunnelte verschlüsslete Websocket
            # Darüber werden daten ohne Anfrage direkt an den verbundenen Client gesendet z.b. Chat Messenger



# --------------     05 - HTTP Request ---------------- #

# 1. Client kommuniziert mit eineem Server über HTTP Rrquest, der unterscheidet sich von Respnse

# Request

# Ein Regest besteht immer aus 3 Teilen. 

# 1. General
#   URL, Method: GET, 
#   GET: Fragt an 
#   POST: Füht was der Resurce hinzu z.b neue Daten
#   DELETE: Löscht einen Inhalt
#   PUT: Updatet ein gesamten Beitrag
#   PATCH: Updatet nur ein bestimmtes Feld

# 2. Header
#   Accept: text/html
#   Accept-language: de-DE
#   Authentication:SZS9XHv8RKdM

# 3. Body
#   {"name":"John", "age":30, "car":null}


# Respnse

# 1. General
#   STATUS CODE: 200 HTTP/1.1 (alles okay)

# 2. Header
#   content-type: text/html; charset=utf-8
#   date: Sun, 24 Oct 2021 09:08:24 GMT

# 3. Body
#   <html><head> ... </body></html>

# Alle Resuquest einer Website lassen sich über die Entwickler tools ein sehn, unter

# Network -> Fetch/XHR 



# ---------------   06 - HTTP Request angucken  ---------------------#

# Alle Resuquest einer Website lassen sich über die Entwickler tools ein sehn, unter, der wichtigste punkt für Backend Entwickler

# Network -> Fetch/XHR 

# wichtige Status codes : https://de.wikipedia.org/wiki/HTTP-Statuscode

# Requestheaders sind die Cariablen die wir an den Server senden.
# ResponseHeaders ist die Antwort die uns der Server zurück meldet
#   acces-control-allow-origin: * (jeder URL darf darauf zugreifen)

# 👉 Hier gehts zu XMLHttpRequest 
# https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest?retiredLocale=de
# 👉 Hier gehts zu AJAX 
# https://developer.mozilla.org/en-US/docs/Glossary/AJAX?retiredLocale=de
# 👉 Hier gehts zu XML Extensible Markup Language 
# https://en.wikipedia.org/wiki/XML


# -------------------   07 - HTTP Status Codes --------------------#

# Wo finde ich die Status Codes :
# https://de.wikipedia.org/wiki/HTTP-Statuscode

# Was bedeutet Grob ein Status Meldung 

# 100 - 105 Information noch in bearbeitung in der regel

# 200 - 299 Erfolgreiche 
#   200 = OKay
#   201 = Created (wenn man ein to do per HTTP sendet)
#   204 = no content

# 300 - 399 Redirection Message
#   301 = Move permernatly, wenn eine webiste permernant umgeleitet wird.

# 400 - 499 Client error (by User or Divice)
#   401 = Unauthorizit Forbidden = keine erlaubnis, keine autoriesierung
#   402 = Payment Requiered, bezahlung notwendig
#   403 = forbidden = aktion not allowed
#   404 = Page noz found, inhalt nicht vorhanden 
#   405 = Methode not allowed
#   429 = To Many Request = zuvieles anfragen = Schutz vor Dodos atacken

# 500 - 599 Server Error
#   500 = Internal server Error, The Server has encountered a sitituation it 
#           does noz know how to handle = Server nicht erreichbar
#   501 = Not implementet = wenn funktion noch nicht fertig sind z.b. 
#   504 = Gatewate timeout, häufig wenn es unendlich läd z.b. 



# ----------------   08 - API verwenden --------------------- #

# Free Api Test im Browser
# https://apipheny.io/free-api/

# 1. Installiere die Corme Extention Jasson Formatter um die visualisierung besser dar zu stellen. 

# 2. Die URL ist in der regel schon der HTTP request, durch abwandeln der URL 
#    an den richtiegen stellen, ändert man die anfrage, sprich die varaibelen

# 3. Im Webbroweser kann man nur GET request testen keine Post Requests, dafür ist Postman zu verwenden.

# 4. Fatch in Java Script JS im Frontend selber anlegen 

# <script>
#  async function init() {
#       let url = 'https://api.zippopotam.us/de/81669';
#       let resp = await fetch(url);
#       let json = await resp.json();
#       document.write('<div> country is ${json.country}<div>');
#       };

#       init();
# </script>


# ------------------   09 - Content Type Header  ------------------- #

# Damit sagen wir dem Server was für einen Typen wir haben wollen!
# Meistens vordern wir ein JSON an, kann aber auch anders aussehn.

# z.b. myapi.com/users/1
# Dies wird in der Regel mit einer Frontend Aplication aufgeruffen, die diese URL aufgeruft. Android App, Iphone App.
# Die Anfrage wird in der Regel mit einem Content Type versendet
# Daten werden häufig in JSON oder XML zurück gegeben. 

# Vergeleich.

# XML:

# content-type: application/XML

# <useres>    
#     <name address="Rosenheimerstr. 139">Junus</name>
#     <name address="Rosenheimerstr. 139">Pascal</name>
#     <name address="Rosenheimerstr. 139">Tom</name>
#     <name address="Rosenheimerstr. 139">Paul</name>
# </useres>


# #JSON:

# content-type: application/JSON

# [
#     {
#         "name" : "Junus"
#     }
# ]

# oft verwendete Contenet-Types:

# content-type: text/html; charset=UTF-8
    # Was bedeutet das?

    # Damit wird angegeben, dass der Inhalt HTML-Code ist.

    # text/html → Der Inhalt ist HTML.
    # charset=UTF-8 → Die Zeichenkodierung ist UTF-8. Damit können beispielsweise auch Umlaute wie ä, ö und ü korrekt übertragen werden.


# content-type: multipart/form-data; boundary=something
    # Dieser Content-Type wird häufig verwendet, wenn ein HTML-Formular Dateien und andere Formulardaten an einen Server übermittelt.

    # Zum Beispiel:

    # Name
    # E-Mail-Adresse
    # Profilbild
    # PDF-Datei

    # Was ist boundary?

    # Die Boundary ist ein Trennzeichen, das die einzelnen Datenbereiche voneinander abgrenzt.


# content-type: application/x-www-form-urlencoded
    # Hier ist eine wichtige Unterscheidung:

    # form-data allein ist kein vollständiger, standardisierter HTTP-Content-Type.

    # Wenn du ein normales HTML-Formular ohne spezielle Dateiuploads abschickst, wird häufig folgender Content-Type verwendet:


# content-type: application/JSON
    # Das ist einer der wichtigsten Content-Types bei modernen REST-APIs.

    # Er bedeutet:

    # „Die Daten sind im JSON-Format.“

    # JSON steht für JavaScript Object Notation.

    # Es ist ein textbasiertes Format, um strukturierte Daten zu übertragen.


# content-type: application/XML
    # Dieser Content-Type bedeutet:

    # „Die Daten sind im XML-Format.“

    # XML steht für Extensible Markup Language.

    # XML kann ebenfalls strukturierte Daten darstellen, verwendet aber sogenannte Tags.
