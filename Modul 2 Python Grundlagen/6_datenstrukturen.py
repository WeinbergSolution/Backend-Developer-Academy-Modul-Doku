#----------------- Datenstrukturen -----------------#


# ---------------    Listen  --------------------- #
# Listen sind eine der wichtigsten Datenstruktur die wir in Python verwenden.

# In einer Liste können Strings, floats, boolean, integer, ander datenstrukturen oder auch andere list und objecte gespeichert werden.

# Die Rheinvolge in der die Elemente in eienr Liste gespeichert werden spielt eine wichtiege Rolle.

# Listen sind sehr Dynamisch man kann beliebig viele Elemente auch zur laufzeit einer Liste hinzugügen. 

# Es muss nicht zu beginn einer Laufzeit fstgelegt sein wie viele Elemente eine Liste enthält. später läst sich herauslöschen, hinzufügen.

# Die verwendetet Datetypen sind sehr felxibel da sie nicht zum beginn der Laufzeit definiert sein müssen wie es z.b. in Js der fall ist.


# Wie wird eine Liste definiert?:
[]              #leere Liste
# Listen können eine Variable zugeordnet werden:
liste = [42, "Pascal", True]

# Liste Anzeigen oder Ausgeben:
len([42, "Pascal", True])  # gibt die Anzal der enthaltenen Elemente zurück 3

# Liste Ausgeben wenn in einer variable gespeichert:
print(len(liste)) # printet die Anzal der enthaltenen Elemente zurück

# Beispiel: 
gerade = [0, 2, 4, 6, 8, 10]
print(len(gerade))           # Aushabe = 6

# Einzelne Elemente aus einer Liste ausgeben durch Index indexindizierung:
# Ausgabe von vorne gezählt:
print(gerade[2])             # gibt das 3 Element aus der liste aus 
print(gerade[20])            # fehler List index out of Range 
# Beim adressieren einzelner Index werte muss der Index exitieren, anders ist es bei sliceing.

# Ausgabe von hinten gezählt:
print(gerade[-2])            # gibt das 2 Element von hinten aus

# Mehrer Elemente aus der Liste raus slicen mit start und end index. slice gibt eine Liste zurück []
print(gerade[0:4])          # gibt die Elemente 0-3 aus als liste = [0, 2, 4]
print(gerade[2:5])          # gibt die Elemente 0-3 aus als liste = [4, 6, 8]
print(gerade[2:11])    # gibt die Elemente 0-3 aus als liste = [4, 6, 8, 10]
# Es ensteht kein fehler wenn man über den End-index hinaus gehn.

print(gerade[-100:11])# gibt die Elemente 0-5  als liste = [0, 2, 4, 6, 8, 10]
# Es ensteht auch fehler, wenn man mit einem -Index begint der nicht existiert.

# beim slicen wenn man beim Index 0 beginnt kann der Start index weg bleiben:
print(gerade[:4])          # gibt die Elemente 0-3 aus als liste = [0, 2, 4]





#-----------------------  Listen Methoden ----------------#

# konkatination "+"      = 2 oder mehrer listen zusammen führen
# append()              = Ein Element der liste hinzufügen:
# sort()                = Sortieren in Aufsteigender Rheinfolge
# sort(reverse=True)    = Sortieren in absteigender Rheinfolge
# count()               = Zählt wie oft das gleiche Element vorkommt
# remove()              = entfernt einen Einzelnen Eintrag aus der Liste
# insert()            = fügt ein Element an einer Index position der Liste hinzu
# clear()               = leert die gesamte Liste
# copy()            = legt eine echte kopie der Liste oder anderew Datentypen an
# in                    = prüft ob ein Element in einer Liste vorhanden ist
# index()              = sucht an welcher index stelle sich ein Element befindet
# join()                # Fügt eine String liste, zu einem String zusammen

## -----Listen Elemente hinzufügen------##

# konkatination +
# Variante 1 konkatination, das aneinander ketten mit dem "+" 
# Listen müssen für die konkatination nicht in Variablen gespeichert sein.
zahlen = [1, 2, 5, 6, 9]
weitere_zahlen = [0, 10, 12, 12]

ergebnis = zahlen + weitere_zahlen

print(ergebnis)

#Listeinträge Multiplizieren *
bits = [0, 1]
print(bits * 3)         # Asugabe = [0, 1, 0, 1, 0, 1]


# append() Methode 
# Ein Element der liste hinzufügen:
nummern = [9, 2, 3, 4 ,5]      # der Variable nummern wird eine Liste zugeordnet
nummern.append(6)              # .append() fügt ein Element ans Ende der Liste
print(nummern)                 # Ausgabe = [9, 2, 3, 4 ,5, 6]

nummern.append(6, 7, 8)    # typeErroe: list.append() takes exactly one argument

## -----Liste Sortieren------##

# Die Methode sort() wendet die Sortierung direkt auf die Liste an, dies muss nicht extrea in eine Variable zwischen gespeichert werden. 

# Sortieren in Aufsteigender Rheinfolge
# sort() 
nummern.sort()              # sortiert die liste / ohne Parmeter aufsteigend
print(nummern)              # Ausgabe = [2, 3, 4, 5, 6, 9]

# Sortieren in absteigender Rheinfolge
# sort(reverse=True) 
nummern.sort(reverse=True)              # sortiert die liste / absteigend aufsteigend
print(nummern)              # Ausgabe = [9, 6, 5, 4, 3, 2]


## -----Anzahl gleicher Elemente in einer liste------##

# count() Zählt wie oft das gleiche Element in der Liste vorkommt, benötigt ein Parameter / das Element das man zählen will
# count()

print(nummern.count(9))     # Ausgabe = 1 / Count gibt immer ein Integer zurück.
print(nummern.count("Pas"))     # Ausgabe = 0 / kein String "Pas" in der Liste


## -----Eintrag aus Liste entfernen / löschen------##

# remove() entfernt einen Einzelnen Eintrag aus der Liste, suce beginnt vorn benötigt als Paramter das Element welches entfernt werden soll

nummern.remove(5)       # Entfernt aus der Liste das Element das den Wert 5 hat 
nummern.remove(9)       # Entfernt aus der Liste das Element das den Wert 9 hat
print(nummern)          # Asugabe = [6, 4, 3, 2] / die 5 wurde entfernt


## -----Eintrag an eine bestimte stelle der Liste hinzufügen------##

# insert()
#insert() fügt ein Element an einer Index position der Liste hinzu.
# Benötigt werden 2 Parmeter, der Index wo das Element eingefügt werden soll & als 2. was.

nummern.insert(0, 10)   # fügt an indexposition 0 das List Element 10 ein
print(nummern)          # Ausgabe = [10, 6, 4, 3, 2]


## -----Gesamte Liste leeren------##

# clear() leert die gesamte Liste
# clear()

nummern.clear()         # Leert die gesamte Liste 
print(nummern)          # Ausgabe = []



## -----Kopie einer Liste erzeugen------##

# Mit copy() wird eine echte Kopie eienr Liste erzeugt und nicht nur ein verweis auf eine andere variable durchgeführt.
#copy()

nummern = [12, "PAscal", 5, "Test"]

kopie = nummern.copy()   # erzeugt eine kopie und legt sie in die Variable kopie
kopie.clear()           # leert die Kopie, ohne den inhalt in nummern zu löschen
print(kopie)             # Ausgabe = [] 
print(nummern)           # Ausgabe = [12, 'PAscal', 5, 'Test']



## -----Nach der Index Position eine bestimmten Elemnts sucehn------##

# Achtung: Erst Prüfen mit "in", ob das element das ich mit index() suchen möchte, in der liste vorhanden ist, um ValueError zu vermeiden.

# index() sucht an welcher index stelle sich ein Element befindet
# index() liefert einen index wert zurück, der in einer Variable gespeichert werden muss oder geprintet werden kann.
# index()

position = nummern.index(5)     # der index an der sich die 5 befindet wird in  
                                # position gespeichert, da index ein wert zurück gibt

print(position)                 # Ausgabe = 2  / die 5 befindet sich auf index 2

# Sucht man den Index eines Elements, welches nicht vorhanden ist in der Liste gibt es ein ValueError

position = nummern.index("hund") 
print(position)           # Asugabe =ValueError "hund" is not in list       

# um den ValueError garnicht erst zu erzeugen scheun wir zuerst in der Liste ob das Gesuchte Element vorkommt mit dem Keyword "in"



## ----- Prüfen ob Element in liste------##
# in gibt immer einen True oder False zurück, da geprüft wird ob vorhanden.
# in
print("pascal" in nummern)   # pruft on "Pascal" in der Liste vorhanden ist
                             # Ausgabe = False



## -----String Liste zu einem String zusammenführen mit------##

# join() kann nur auf eine Liste mit Strings angewendet werden, bekommt 2 Paramter, das trennzeichen ";" und eine Liste (liste). 
# Wendet man join() auf eine Liste mit anderen Datentypen an, kommt es zu einen TypeError

#join()
print(";".join(nummern))     # Ausgabe = TypeError, sequence item0: expected 
                             # str instance, int found

nummern.clear()              # leert die liste nummern
nummern = ["pascal", "hans", "Paul"]    # weist nummern eine neu Liste hinzu

print(";".join(nummern))       # Aushabe = pascal;hans;Paul
print("".join(nummern))       # Aushabe = pascalhansPaul






#-----------------------  tuple ----------------------------------#

#Tuple's ist ein Datenstrucktur die relativ star ist.
# Tuple können Strings, Integer, boolen, usw beinhalten.
# Es können keine Elemente hinzugefügt oder entfernt werden.
# Tuple werden verwendet um eine Fixe anzahl an Elementen in eienr Datenstruktur zu speichern, die nicht veränderbar ist.
# Hat eine funktion mehrere Rückgabewerte, wird es als Tuple zurück gegebn.
# Elemente lassen sich auslesen, jedoch nicht hinzufügen oder löschen.
# EIn Tuple entspricht mathematisch betrachtet einen Vektor

# WIe wurd ein Tuple erzeugt ? = ()
()                                    # = leeres Tuple
print(len())                          # Ausgabe =  ()

test = (42, 1.5, True, "Florian")    
print(len(test))                      # Ausgabe = 4

test2 = (1, 2, 5, 7, 28, 29, 1, 1, 1, 8)
print(test2[:3])                      # Ausgabe = (1, 2, 5)

print((1, 2, 5, 7, 28, 29, 1, 1, 1, 8)[-4]) # Ausghabe = 1 / 4 index von hinten 


def addieren(a, b):             # Funktions Kopf
    summe = a + b               # a + b wird in summe gespeichert
    return a, b, summe          # a, b, summe wird in einem Tuple zurück gegeben
                                # da mehr als ein rückgabewert existiert

ergebnis = addieren(1, 4)       # funktion addieren wird mit den Parametern 
                                # 1 und 4 ausgeführt und das Ergebnis in ergebnis gespeichert 

print(type(ergebnis))           # printet den Datentype welcher sich in der 
                                # ergebnis sich befindet 
                                # Ausgabe = <class 'tuple'>


# Weiteres Beispiel mit Tuple () und args Parameter *
# args Parameter gibt immer ein Tuple zurück, da Python nicht weiß wie viele Paramter kommen werden. 

def addieren(*summanden):       # Funktions Kopf mit dem args * paramter 
  sum(summanden)
  print(type(summanden))        # printed den Datentype von summanden, wenn 
                                # die funktion aufgeruffen wird

addieren()                      # Funktionsaufruf



#--------------------   Tupel Methoden   -----------------------#

#  konkatination +     = mehrer Tupel zusammen führen 
# count()              = Zählt wie oft das gleiche Element vorkommt
# index()              = sucht an welcher index stelle sich ein Element befindet
# copy()           = legt eine echte kopie der des Datentyps an heir ein tuple
# smple kopie          = Tuple ist unveränderbar, einfach in neue variable spei.
# tuple sortiern       = erst in eine liste umwandeln dann sort() anwenden 


## ------------------- Tuple zusammen führen -------------##

# konkatination +
# Variante 1 konkatination, das aneinander ketten mit dem "+" 
ergebnis = (1, 2, 3) + (4, 5)   # Tuple zusammen führen & in eergebnis speichern

print(ergebnis)                 # Ausgabe = (1, 2, 3, 4, 5)


## ---------------Anzahl gleicher Elemente im Tuple ausgeben -------------##

# count() Zählt wie oft das gleiche Element in dem tuple vorkommt, benötigt ein Parameter / das Element das man zählen will
# count()
tuple = (2, 3, 5, 7, 9, 11, 13, 2, 5, 7, 7, 0, "pas")  # ein tuple wird in tuple gesp. 
n = tuple.count(7)                    # Zählt wie ift die 7 im tuple vorkommt

print(n)                              # printet die n, n enthält die anzahl

#count lässt sich auch direkt am Tuple anweden ohne zwischen variable.


## -------Suchen an welcher index stelle sich ein wert bedinet  -------------##

# index() sucht an welcher index stelle sich ein Element befindet
# index() liefert einen index wert zurück, der in einer Variable gespeichert werden muss oder geprintet werden kann.
# index()

print(tuple.index("pas"))           # Ausgabe = 12

## -----Kopie eines tuple erzeugen------##
# Tuple ist eine unveränderbare datenstrucktur daher kann man eine kopie einfach in ein neue variable speichern ohne copy() zu benutzen.
# Da keine änderung auf dem Tuple durchgeführt werden können kann man einfach mit dem Zeiger also einer 2 variablen arbeiten,
#da man die uhrsprungsvariable oder die Kopie nicht veränder bar ist.
# copy() kann dennoch angewendet werden.

zahlen = (16, 12, 1989)             # erzeugt ein tuple speichert in zahlen

kopie = zahlen                      # tuple aus Zahlen, wird in Kopie gesp.

print(kopie)                        # Asugabe = (16, 12, 1989)


## ------- Tuple Sortieren / möglich ? / erst in liste umwandeln -----##

# list() ist ein funktion um z.b. ein Tuple oder andere Datentypen in eine liste umzuwandeln. 
# list()
wetre = (5, 10, 50, 30, 62, 15)       # tuple in der variable werte gespeichert.

print(type(list(zahlen)))         # Ausgabe = <class 'list'>

print(list(zahlen))               # wandelt das tuple aus zahlen, in eine liste
                                  # Ausgabe = [16, 12, 1989]


# Nun kann man wieder die Sort() & sort(reverse=True) anwenden um die Liste aufsteigend oder absteigend zu sortieren. 
# siehe sort() Metode  unter list Methoden, weiter oben. 
liste = list(zahlen)            # ereugt aus dem Tuple in zahlen, eine liste

liste.sort()                    # sorttiert die liste aufsteigen

print(liste)                    # Ausgabe = [12, 16, 1989]




# ------------------------- sets -----------------------------#

# Set() wird häufig in der schleifen Prüfung verwendet, ob ein element schon gesehn wurde z.b. 
# Sets ist ein Weiterer Datentüp 
# Sets ist nix anderes als eine Menge. 
# Diese Menege hat keine interne  Rangfolge.
# Werte können zwar dopplet im set stehn, werden aber nur 1 mal ausgegebn.
#  
# wichtig: ein leeres set wird so defieniert set() / {} dies wäre ein Dictonary

# konsturktor aufruf set() erzeugt ein leeres set ist es nicht leer verwendet man {} z.b. {12, 28, 39}
# set()

set()                       # erzeugt ein leeres set

                            # printed ein gefülltes set {}
print({12, 28, 39, 3, True, "pas",})   # Ausgabe = {True, 3, 39, 'pas', 12, 28}

print(len({12, 28, 39, 3, True, "pas", 12}))   # Ausgabe = 6 obwohl 7 vorhanden.
                                               # doplete werden nicht ausgegeb
                    




# ------------------ Sets Methoden ---------------------------#

# in                    = prüft ob ein Element in einem set vorhanden ist
# add()                 = Fügt einem set ein Element hinzu 
# remove()              = Ein element aus dem set  löschen.
# clear()               = Leert das gesamte set 
# copy()                = Erzeugt eine Echte kopie von set, da, 
#                         da ein Zeiger oder verweis auf eine ander Variable
#                         nicht ausreicht, und den urspurng verändert 



# in
# in gibt immer einen True oder False zurück, da geprüft wird ob vorhanden. 
 
zahlen = {1, 4, 6, 7, 8}        # erzeugt ein set und speichert es in zahlen

print(99 in zahlen)             # prüft ob 99 in dem set {} in zahlen vorkommt.
                                # Ausgabe = False


# add() 
# add() fügt dem set {} ein Element hinzu 

zahlen.add(-1)                  # fügt dem set in zahlen die -1 hinzu.

zahlen.add(4)                   # macht nix, da 4 schon im set {} vorhanden war.

print(zahlen)                   # Asugabe = {1, 4, 6, 7, 8, -1}


# remove()  
# remove() entfernt ein definiertes Element aus dem set {} benötigt den Parameter der gelöscht werden soll.

prim = {2, 3, 5, 8, 11}         # erzeugt ein gefültes set & savet es in prim

prim.remove(5)                  # enternt die 5 aus dem ste {} in prim

print(prim)                     # Asugabe = {2, 3, 8, 11}


# clear()
# clear () leert das gesamte set, so wie es bei listen oder tuples der fall ist.

prim.clear()                    # leert das gesamte set {}

print(prim)                     # Ausgabe = set()


# copy()
# Mit copy() wird eine echte Kopie eiens set erzeugt und nicht nur ein verweis  auf eine andere variable durchgeführt.


prim = {2, 3, 5, 8, 11}          # erzeuge ein gefüültes set, saved in prim

kopie = prim.copy()              # Erzeugt eine Kopie, kein verweis

kopie.celar()                    # leert die erzeugte kopie

print(prim)                      # Ausgabe = {2, 3, 5, 8, 11}
                                 # das leeren der kopie, hat nicht prim gelert.



#sort() & sort(reverse=True)
# Um sort() auf ein set anzuwenden, muss das set erst wieder in eine Liste umgewandelt werden. list()

prim = {12, 7, 5, 8, 11}         # erzeugt ein gefülltes set, saved in prim

liste = list(prim)              # wandelt das set in prim, in eine liste

liste.sort()                    # sortuert die liste aufsteigend

print(liste)                    # Ausgabe = [5, 7, 8, 11, 12]





# ----------------- Dictionaries --------------------------#

# Dictonary = Wörterbuch, muss man sich genau so vorstellen
# Dictonarys sind ansammlung von Schlüssel Wert Paaren. 

# Ein Dictonary wird mit den {} erzeugt in denen sich Schlüssel wert Paare befinden.

# der Schlüssel muss ein Primitiver Datentyp sein und mit einem : von einander getrennt. str, int, flot, boolen / flot, boolen nicht nehm.

# DEr Wert kann Diverse Datentypen enthalten.
#z.b. String, Integer, listen[], tuple(), set(), dictonarys {}, usw
# Ruft man den Schlüssel auf, mit.get(), wird der Wet ausgegeben.


telefonbuch = {          # Erzeugt ein Dictonary & weißt sie der variable hinzu
   "Pascal" : "017672764302",        # "schlüssel" : "Wert" Paar
   "Pascal2"    : 17672764302,
   "tuple"      : (1, 2, 3),
   "Liste"      : [12, "hallo"],
   "set"        : {12, 16, True},
   "dictonary"  : {"Pascal" : "017672764302"},
   1            : 23,
   1.0          : "Pascl",      # benutzt man in der Regel auch nicht.        
   True         : "Warheit",    # boolen kann nur 2 werte liefern, nicht nehm
   False        : "Lüge"


}


# Auslesen von werten mit .get() / immer verwenden wenn nicht bekannt ist ob der Schlüssel vorhadnen ist im Dictonary.
print(type(telefonbuch.get("Pascal")))  # Ausgabe Datentyp = <class 'str'>
print(telefonbuch.get("Pascal"))        # Ausgabe = 017672764302 as String
print(type(telefonbuch.get("Pascal2"))) # Ausgabe Datentyp = <class 'int'>
print(telefonbuch.get("Pascal2"))       # Ausgabe = 017672764302 as Integer
print(telefonbuch.get("hund"))          # Ausgabe = None / kein KeyError
# Das None lässt sich später über eine Schleife abfanegn. 

# Auslesen mit direkt adressiertung [], kann zu einem KeyError führen wenn nicht der Schlüssel nicht existiert, .get() verwenden.
print(telefonbuch["Liste"])             # Ausgabe = [12, 'hallo']
print(telefonbuch["hund"])             # Ausgabe = KeyError 'hund' / nicht da


#len()
# Anzahl der Schlüssel Wert Paare Ausgeben

print(len(telefonbuch))                 # Ausgabe = 8




# ----------------   Dictionary Methoden  ----------------------#

# .get()           = Liest ein Wert anhand der Schlüssels aus
# []               = Direkt Adressierung / kann ein KeyError erzeugen

# update()         = Aktualisiert den Wert eines Schlüssels
#[] = ""           = Aktualisiert auch, wenn key aber nicht vorhanden
#                    wird ein neues Key-Value Pair hinzugefügt. 

# del              = Löscht einen schlüssel und dessen Wert 
# clear()          = Löscht das Gesamte Dictonary
# copy()           = Erzeugt eine Echte Kopie, keinen Pointer

# keys()           = Gibt alle Schlüssel, die sich im Dictonary befinden aus.
#                    Erzeugt ein eigenen Datentyp = dict_keys
#                    liber in liste Umwandeln

# value()           = Gibt alle Value, die sich im Dictonary befinden aus.
#                    Erzeugt ein eigenen Datentyp = dict_value
#                    liber in liste Umwandeln






passwort_hashes = {
"abc123" : " e99a18c428cb38d5f2",
"1337" : "e48e132e7341b6bffb7" ,
"love" : " b5ceb187fe309aføf"
}


## ------- Werte an hand des Schlüssels auslesen ------##

# .get()     oder direkt Adressierung [] kann zu fehlern führen
# Mit get() kann man Werte aus dem Dictonary auslesen ohne eine KeyError zu erzeugen wie es bei der direkt Adressierung [] vorkommen kann.

print(passwort_hashes.get("love"))   # Ausgabe =  b5ceb187fe309aføf

print(passwort_hashes.get("geheim"))   # Ausgabe =  None
print(passwort_hashes["geheim"])   # Ausgabe =  KeyError / .get() nehm.

# Es ist möglich einen default Wert einen Key mit zu geben wenn dieser im dictonary nicht vorhanden ist.

print(passwort_hashes.get("geheim", "!545!"))   # Ausgabe =  "!545!"


# --------- Wert einens Schlüssels ändern -------------##

telefonnummern = {
   "Junus" : "014578695474",
   "Flo"   : "015457898654",
   "Tom"   : "015488796587"
}

# Werte können mit der Direkadressierung und dem Zuweisungs Operator = geändert werden.
# Achtung : gibt es den KEy nicht, wird ein neues KEy-Value Pair angelegt.

telefonnummern["Eva"] = "01905554888"   # Neues KEy-Value Pair wird angelegt

print(telefonnummern)                   # Ausgabe {'Junus': '014578695474', 
                                        # 'Flo': '015457898654', 'Tom': '015488796587', 'Eva': '01905554888'}


# update() bekommr ein Dictonary als übergabe Parameter
# update() ist die bessere Variante um den Wert eines Keys neu zu setzen.
# 

telefonnummern.update({"Tom" : "99999999"})     # Der KEy Tom, bekommt ein 
                                                # Wert, durch das überschriebn des geasnten Dictonary Eintrags

print(telefonnummern.get("Tom"))                # Ausgabe = 99999999



# -------- Schlüssel aus dem Dictonary Löschen ---------#

# Mit del, lässt sich ein Key und sein Value aus dem Dictonary Entfernen.
# del benötigt einen Key als Übergabeparameter in [] klammern.
# Versucht man einen KEy zu löschen, der nicht existiert, passiert nix, auch kein Fehler.

del telefonnummern["Tom"]          # löscht das Key-Value Pair mit dem Key "Tom"
del telefonnummern["Eva"]          # löscht auch Eva raus

print(telefonnummern)              # {'Junus': '014578695474', 'Flo': 
                                   # '015457898654'}



# -------- Gesamtes Dictonary leeren --------------------#

# clear() leert das geasmte Dictonary
# clear() 

test = {"Pasca" : "hund"}           # Erzeugt ein Dictonary

test.clear()                        # Leert das gesamte Dictonary

print(test)                         # Ausgabe = {}


# ------- Echte Kopie eine Dictonarys erzeugen -----------#

test = {"Pasca" : "hund"}           # Erzeugt ein Dictonary

kopie = test.copy()                 # Echte Kopie erzeugen

kopie.clear()                       # Kopie löschen, da kein pointer
                                    # ändert sich an dem Dictonary in test nix.

print(kopie)                        # Ausgabe = {}
print(test)                         # Ausgabe = {'Pasca': 'hund'}


# -----Rausfinden welche SChlüssel sich im Dicronary befinden ------#


# keys()
# keys() listet die Schlüssel auf, die in einem Dictonary vorhanden sind, gibt allerdings den Datentyp "dict_keys" zurück.

print(type(test.keys()))            # <class 'dict_keys'>
print(test.keys())                  # Ausgabe = dict_keys(['Pasca'])

# Alternativ in eine Liste umwandeln um besser damit weiter arbeitn zu können.

print(list(test.keys()))            # Ausgabe = ['Pasca']


# ------ Alle Werte Augeben die sich im Dictonary befinden -------#

#value()
# Value() listet alle Werte auf die sich in einem Dictonary befinden. Gibt diese als dict_value zurück.
# Zum weiter verarbieten in liste umwandeln list(test.value())

print(test.values())                # Ausgabe = dict_values(['hund'])

print(list(test.values()))          # Ausgabe = ['hund']


