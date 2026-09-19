#https://developer-akademie.teachable.com/courses/2146966/lectures/48432713


#------------------ Funktionen --------------------------------------

#---------------   Was sind Funktionen? -------------------------------

#Eine Funktion kapselt anwesiung und führt sie aus



# function - fuctionname(übergabe parameter):
# Javascript variante # fuction sag_hallo(name){}
# Python Variante       def sag_hallo(übergabeparameter):
#                           scope wirkungsbereich muss eingerückt sein

# Beispiel 1:
def sag_hallo():     # ist das eqivalent zu fucktion in javascript
    pass         # pass ist ein platzhalter function darf nicht leer sein 
                        # def wird für die definition eine function gebraucht
def sag_moin(vorname, nachname):     # FucktionsKopf endet mit : in js mit {}
    print(f("Hallo {vorname} {nachname}!")) # scope 
 

#f-name (Parameter) / gleich viele Paramter wie im funktionskop  definiert
sag_moin("Pascal", "Weinberg")   # def wird beim aufruf nicht gebraucht

#Beispiel 2:
def addieren(a, b):          #funktionskop
    summe = a + b            #scope
    return summe      # Return gibt was zurück, dies steht dann am anfag
                      # des funktionsaufruf gedanklich

s = addieren(10, 32)    # summe ist ein fremder scope / kein zugriff
print(f"Summe: {s}")

# Was macht die Python-Funktion len?
# Sie berechnet die Länge eines Arrays.
# Sie berechnet die Länge eines Strings.
# Sie gibt die Länge einer Liste zurück




#------------------   args Paramter----------------#
#  args Parameter verwenden beginnt mit (*)
#  args Parameter gibt ein () tuple zurück
# Args Parameter ermöglicht die übergabe von einer Variablen anzahl an Parametern
# Args Parameter werden als leztes angegebn wenn mehrer Parameter davor existiern da Python nicht weiß wie viele Args Parameter existieren


# Beispiel:
def addeiren(summand1, summand2, summand3, summand4, summand5):
    summe = summand1 + summand2
    print(summe)


# Lösung:
#  args Parameter verwenden beginnt mit (*)
# Args Paramter wirft beim funktionsaufruf ohne Paramter kein fehler
# Sondern gibt dann ein leeres Tuple zurück
# Verwende ich zu dem  Args Parameter einen weiteren oder mehrere 
# (name, *summanden) muss mindest ein Parameter im Funktionsaufruf übergeben werden

def addieren_neu(*summanden):    # (*Summand) kann x Parameter entgegennehm     
    print(sum(summanden))        #   (*Summand) gibtg ein Tuple () zurück  
                                 # 

addieren_neu(1,-2,3)             # = 2

addieren_neu()           # kein fehler da * Args Argument allein verwendet wurde

# Verwednet man andere Parameter in kombination mit dem Args *Parameter
# Müssen die anderen Parameter zuerst kommen, 
#Beispiel 2:
def lotto_spielen(vorname, nachname,*lottozahlen):
    print(f"Hallo {vorname} {nachname}")
    print(f"Deine Zahlen lauten: {lottozahlen}")

lotto_spielen(4, 8, 15 , 16, 23, 42, "Pascal", "Weinberg") # alles gut
lotto_spielen("Pascal", "Weinberg") # Alles gut
lotto_spielen("Weinberg") # missing 1 position Argument





#---- --------- kwargs = Keyword argument-----------------#
#  kwargs Parameter beginnt mit (**test)
#  kwargs Parameter geben ein {} dictonary zurück 
#  kwargs Parameter erwartet im funktionsaufruf schlüsselwerte Paaren (a=1, b=2)
#  kwargs Parameter erwartet eine variable anzahl an schlüsselwerte Paaren
#  Bei kwargs Parameter ist die rheinfolge egal da mit Schlüssel gearbeitet wird

def kwargs_test(**test):    # (**) nur bei definition verweden im Kopf
    print(test)             # aufruf von (test) ohne ** im scope

kwargs_test(a=1, b=2, c=5)  # funktionsaufruf mit Schlüsselwert Paaren
                            # Ausgabe = {"a":1, "b":2, "c":3}


# beispiel:
def teilnehmer(vorname, nachname, alter, geschlecht):
    print(f"{vorname} {nachname}; {alter}; {geschlecht}")

teilnehmer("Pasca", "Weinberg", 28, "männlich")

#Lösung: mit kwargs Parameter
def teilnehmer(**daten):
   vorname =  daten.get("vorname")  # schlüssel werden als Strings "" übergeben
   nachname = daten.get("nachname") # schlüssel werden als Strings "" übergeben
   alter = daten.get("alter", 18)   # gibt none oder wenn definiert den default 
                                    # Wert zurück wenn nicht im f-Aufruf 
   geschlecht = daten.get("geschlecht", "N/A") #nicht im f-aufruf = default
   print(f"{vorname} {nachname};{alter}, {geschlecht}")
                   # Auf den kwargs Paramter daten weneden wir die  
                   # .get() Methode an = daten.get()
                   # .get() erwartet den Parameter Schlüssel als String
                   # zb. daten.get("vorname")
teilnehmer(vornamee="Pascal", nachname="Weinberg")
#          schlüssel="Wet"  , schlüssel="Wert"

# Rehienfolhe der Parameter arten
# nomale Parmeter, *args, **kwargs





#------------------- Aufrufreihenfolge in Funktionen ---------------#
# Rehienfolhe der Parameter arten = nomale Parmeter, *args, **kwargs
# 1. normale Parameter = Position Arguments
# 2. *Args Parameter da Python nicht weiß wie viel kommen
# 3. **kwargs Paramter da Python nicht weiß wie viel kommen

# Beispiele: 
def daten_erfassen(id, vorname, nachname, *geo):
    pass

def daten_erfassen2(id, vorname, nachname, **geo):
    pass

def daten_erfassen3(id, vorname, nachname, *geo, **Daten):
    pass

def daten_erfassen3(id, vorname, nachname,  **Daten, *geo,): # fehler Rheinfolge
    pass







# -----------------------   Scoping -----------------------------#

# built-in Scope = Gesamte Python umgebung
# global Scope  = Gesamtes Python Programm
# local Scope   = in einer Funktion

# built-in Scope
# Sobald man den Python interpreter startet und im Interaktiben moddus bist befindest du dich im "built-in Scope"
# Dort hat man auf alle KEywords zugrif die es in Python gibt z.b. import, while, for, if , else und es lässt sich auf intterne Variablen 
# zugreifen


# global Scope
# Global scope erstreckt sich auf eine gesamtes Python Programm
# Der Globale Scope startet ganz am beginn 

#Local Scope
# Variablen aus dem Local scope überschreiben keine Globalen Scope Variablen
# Um aus dem local Scope eine Globale Variable zu ändern, muss sie im local Scope mit dem KEyword "global" bekannt gemacht werden.
# "global level"
# Findent Python im Local Scope die Variable nicht die es sucht, schaut er im Global Scope als nächstes.

#Beispiel: 

level = 0                                   # globaler Scope

def level_up():
    global level            # Globale variable im local scope bekannt machen
    level += 1              # erhohen der bekanntgemacht Globalen Variable 
                            # im local Scope nach bekanntmachung möglich 
           

level_up()
print(f"Dein Level ist: {level}")


# Es gibt auch noch den Endclosing Scope wenn Funbktionen in Funktionen definiert werden, brauch man als anfänger erst mal nicht.






#------------------   Module entwickeln und einbinden --------------#

#Für das Beispiel werden 2 Pyton datein benötigt im gleichen Ordner
# 1. tschenrechner.py
# 2. main.py 


 # taschenrechner.py 

def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    return a / b


# Damit wir die Funktionen aus der taschenrechner.py verwenden können in der main.py benötigen wir das Keyword import taschenrechner 
# Dateiendung .py muss nicht mit angegegnen werden 

# main.py
# importiere taschenrecher als tr   / einen kürzeren alias sozusagen
import taschenrechner as tr

summe = tr.addieren(1, 2)           # = 3
print(summe)

differenz = tr.subtrahieren(5, 2)   # = 3
print(differenz)

produkt = tr.multiplizieren(2, 10)  # = 20 
print(produkt)

quotient = tr.dividieren(20, 4)
print(quotient)


# weitere Variante 

# main.py
# wir importieren vom Modul Taschenrechner * = alles
from taschenrechner import *

summe = addieren(1, 2)           # = 3
print(summe)

differenz = subtrahieren(5, 2)   # = 3
print(differenz)

produkt = multiplizieren(2, 10)  # = 20 
print(produkt)

quotient = dividieren(20, 4)
print(quotient)

# Diese Variante kann ein Nachteil haben, wenn man mehrer Module verwendet mit gleichen funktions namen 




#--------------   if __name__ == "__main__": ---------------------#
# Es erlaubt die Asuführung des Skripts als eigenständiges Programm und als Modul

# Mit dieser Aanweisung kann man definieren das eine Funktion nur ausgeführt wird, wenn sie als Hauptporgramm ausgeführt wird.
# So lassen sich bereiche Ausklammern, die nicht berücksichtig werden wenn etwas als Modul importiert wird. 
# was im Scope dieser Anweisung liegt if __name__ == "__main__": wird ignoriert, solange ein anderes Porgramm das Modul ausführt.

# Beispiel 

# taschenrechner.py 

def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    return a / b

# Dies würde nur ausgeführt werden wenn ich direkt Taschenrechner.py ausführe ansonsten wird es ignoriert
if __name__ == "__main__":      
    print(addieren(1, 2))




#-----------------   input-Funktion   ------------------#
# mann kann aber muss nicht einen Übergabeparamter angeben in den ()
# Wenn man aber einen verwedet, muss er vom Datentypr ein String "test" sein.
# Input liefert immer eine Zeichenkette = String zurück.
# input() ist eine sogenante blockierden Anweisung, kommt das Programm an der stelle an, wird auf die Eingabe des Nutzers gewartet.
#input() kann verwendet werden, damit sich das Programm nicht von selber wieder schließt. 

# Beispiel 1:
name = input("Gib deinen Namen ein: ") #Input wird in die Variable name gesp.
print(f"Hallo {name}")

# Beispiel 2: 
# Zahlen im input() in integer umwandeln, da es sich um das Geburts jahr handelt. 

jahr = int(input("In welchem Jahr wurdes du geboren ? "))

alter = 2023 - jahr

print(f"Du bist {alter} alt. ")

# Benutzer eingaben sind immer etwas kritisches da sie zu Laufzeitfehlnern führen können, da der benutzer was anderes eingibt als erwartet.



#---------------   exec-Funktion ----------------------#
# Wichtig: exec() sollte nicht verwendet werden um Nutzer eingaben zu verarbeiten.

# exec ist eine der gefährlichsten funktion in Python durch String manipulation vor allem wenn der code lang und unübersichtlich wird.
# gefährlich wird es z.b. wenn der code so gestaltet ist das er nicht lesbar auf anhieb ist da er zuvor z.b. in Base64 umgewandelt wurde.

# Beispiel 1:
cmd = "print('Hallo Welt!')"
exec(cmd)

# Beispiel 2:
# durch ein ; können mehrer Anweisung verkettet werden. 
cmd1 = "name = input('Gin deinen Namen ein: '); print(f'Hallo {name}')" 
exec(cmd1)

# Beispiel 3: wo die gefahren stecken 

# normaler lesbarer python code
cmd2 = """
import random

geheime_zahl = random.randint(1, 10)

print("🎮 Willkommen bei 'Zahl erraten'!")
print("Ich habe mir eine Zahl zwischen 1 und 10 ausgesucht.")

while True:
    tipp = int(input("Dein Tipp: "))

    if tipp < geheime_zahl:
        print("⬆️ Zu klein!")
    elif tipp > geheime_zahl:
        print("⬇️ Zu groß!")
    else:
        print("🎉 Richtig! Du hast gewonnen!")
        break
"""
exec(cmd2)

# umgewandelt in base64 und ausführbar
# Damit das möglich ist benötigen wir den import base64
import base64
cmd3 = "aW1wb3J0IHJhbmRvbQoKZ2VoZWltZV96YWhsID0gcmFuZG9tLnJhbmRpbnQoMSwgMTApCgpwcmludCgi8J+OriBXaWxsa29tbWVuIGJlaSAnWmFobCBlcnJhdGVuJyEiKQpwcmludCgiSWNoIGhhYmUgbWlyIGVpbmUgWmFobCB6d2lzY2hlbiAxIHVuZCAxMCBhdXNnZXN1Y2h0LiIpCgp3aGlsZSBUcnVlOgogICAgdGlwcCA9IGludChpbnB1dCgiRGVpbiBUaXBwOiAiKSkKCiAgICBpZiB0aXBwIDwgZ2VoZWltZV96YWhsOgogICAgICAgIHByaW50KCLirIbvuI8gWnUga2xlaW4hIikKICAgIGVsaWYgdGlwcCA+IGdlaGVpbWVfemFobDoKICAgICAgICBwcmludCgi4qyH77iPIFp1IGdyb8OfISIpCiAgICBlbHNlOgogICAgICAgIHByaW50KCLwn46JIFJpY2h0aWchIER1IGhhc3QgZ2V3b25uZW4hIikKCiAgICAgICAgYnJlYWs="

# wir rufen aus dem Import base64 eine funktion auf names b64decode() der übergeben wir die variable in der alles gespeichert wurde "cmd3"
exec(base64.b64decode(cmd3)) 


# Warum ist die Funktion "exec" gefährlich?
# Weil bei fehlender Input-Prüfung potentiell Schadcode ausgeführt werden kann.