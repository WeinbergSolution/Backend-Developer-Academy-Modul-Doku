##--------------------Objektorientierte Programmierung---------------------#

   #----  Einführung in die objektorientierte Programmierung -------#

# Objektprogrammierung hilft dabei kein Spagetti Code zu erzeugen & eine Funktion nach dem andern zu schreiben. 

# Mit der Objektprogrammierung lassen sich Funktionen Clustern.


# Beispiel:
# Wenn wir eine Hund funktionen geben möchten, kann man diese Clustern.
# Und nur die Funktionen Clustern die für den Hund benötigt werden also bündeln.

# Hund
# laufen()
# essen()
# bellen()

# class kann man als schablone betrachten, um z.b. diverse Hunde zu erzeugen, 
# Die alle essen, bellen, laufen können, die funktion teilen sie sich.
# zusätzlich kann man ihnen individuelle eigenschaften mitgeben.

class Hund:                 # erzeugt eine Classe /schablone namens Hund

    # Die __init__ funktion ist bei jeder classe standartmäsig vorhanden und dient dazu ein Objekt von Hund zu erzeugen.

    # die  __init__ funktion erzeugt ein Objekt, welches alle funktionen die definiert wurden beinhaltet und zusätlich eigenschaften.
    # Die eigenschaften können individuell sein, sie werden in der __init__ function als parameter übergeben und im scope definiert.

    def __init__(self, farbe, rasse, name):

        self.farbe = farbe  # self.farbe ist eine zuweisung an das aktuelle 
                            # / = farbe der Übergabeparameter der beim aufruf der __init__ mitgegegn wird     
                             
        self.rasse = rasse

        self.name = name

    def vorstelen(self):
        print(f"ich bin {self.name}")

    def essen(self):        # funktion essen mit Parameter self
        pass                # pass = Platzhalter für leere function

    def bellen(self):       # funktion bellen mit Parameter self
        pass                # pass = Platzhalter für leere function   

    def laufen(self):       # funktion laufen mit Parameter self
        pass                # pass = Platzhalter für leere function   


# Dadurch lassen sich jetzt diverse Objekte von Hund erzeugen, die alle essen, bellen & laufen könne.
# Darüber hinaus einzigartige Eigenschaften haben können die bein funktionsaufruf __init__(self, farbe, rasse, name) übergebn werden.

# Beispiel: 

dog1 = Hund("Braun", "schäferhund", "Passol")
dog2 = Hund("Weiß", "Dackel", "Wuffi")

# dog1 & dog2 sind eigenständiege instanzen, sie haben zwar den gleichen funktiosumfang aberr idividuelle Eigenschaften.
# Das hat den vorteil das sich sehr sauberer Software Code schrieben lässt.

print(dog2.vorstelen())      # Ausgabe = ich bin Wuffi




# 1. Eine Klasse ist ein Bauplan für Objekte.
#    In ihr legen wir fest, welche Eigenschaften
#    und Fähigkeiten spätere Objekte besitzen.

class Kind:

    # 2. Der Konstruktor (__init__) wird automatisch
    #    beim Erstellen eines neuen Objekts aufgerufen.
    #    Hier erhalten die Objekte ihre individuellen
    #    Eigenschaften (Attribute).

    def __init__(self, alter, name, groesse, spezial):

        # self verweist immer auf das aktuelle Objekt.
        # Attribute werden mit self gespeichert.

        self.alter = alter
        self.name = name
        self.groesse = groesse
        self.spezial = spezial

    # 3. Funktionen innerhalb einer Klasse heißen Methoden.
    #    Sie beschreiben, was ein Objekt tun kann.

    def laufen(self):
        print(f"{self.name} läuft.")

    def rennen(self):
        print(f"{self.name} rennt.")

    def spezialkraft(self):
        pass
        


# ============================================
# Objekte (Instanzen) erstellen
# ============================================

# Die Klasse ist der Bauplan.
# kind1 und kind2 sind zwei verschiedene Objekte.

kind1 = Kind(10, "Max", 140)
kind2 = Kind(12, "Lisa", 152)


# ============================================
# Zugriff auf Attribute
# ============================================

print(kind1.name)       # Max
print(kind1.alter)      # 10
print(kind1.groesse)    # 140


# ============================================
# Methoden aufrufen
# ============================================

kind1.laufen()
kind2.rennen()
        




 ##--------------- Vererbungungen-----------------#
# Wenn Funktionen so algemein sind, das sie auf mehrer Klassen Anwendbar sind, 
# wie z.b. Laufen und springen bei Tieren und man verschieden Tier Klassen hat, 
# Kann man eine übergeordnete Klasse erstellen die diese Funktion beinhalten und dann an die anderen Klassen weiter Vererbt. 

#Beispiel: Stell dir vor es gibt jeweils eine Class Hund & Katze, beide haben eigenschaften die beide verwenden.
# Dann macht es Sinn eine Überklasse zu erzeugen z.b. Säugetiere

# Vererbung example
#      Säugetier
class Mamal:

    def __init__ (self, farbe,rasse, name):
        self.farbe = farbe
        self.rasse = rasse
        self.name = name

    def vorstellen(self) :
        print(f"lch bin {self.name}")

    def essen(self):
        pass


class Hund(Mamal):

    def bellen(self):
        pass

    def laufen(self):
        pass

class Katze(Mamal):

    def miauen(self):
        print('Miau!!!')

dog1 = Hund('Braun', 'Schäferhung', 'Fritzi')
dog2 = Hund('Schwartz', 'Schäferhund', 'Wuffi')
cat1 = Katze('Weiß', 'Britisch kurz Haar', 'Mina')

dog2.vorstellen()
cat1.vorstellen()
cat1.miauen()




#------------------   Pokémon Teil 1 ---------------#
# Jedes Pokemon ist ein Ojekt. 

class Pokemon:

# __init__ = Konstruktor in Python = Magische Methode
# Die __init__ Methode ist das was als erstes Durchlafuen wird, wenn ein Objekt Instanziert wird.  

#Damit aus einer Normalen Variable eine Objektvariable wird benötigen wir das wort "self", das equivalent in js in "this"
                #self instanz aufrufen 
    def __init__(self, name, level, stärke):
        self.name = name        # was hinter dem self. steht wird einer 
                                # ObjectVariable zugewiesen 
        self.leve = level
        self.__stärke = stärke  # geschütze Obj.Variabel, kann nicht einfach 
                                # drauf zugegriffenm werden, für den 
                                # Zugrif bracht man eine extra Methode und get

        self.vorstellen()       # 

# Im kontext der Projektorientierten Programmierung heißen Funktion, Mehoden
# Erzeugen wir eine Methode brauchen wir dei "self" Instanz, dies definiert das die Methode zu einem Objekt gehören. 
    def vorstellen(self):
       print(f"{self.name}, {self.name}!")  # Self.name bezieht sich auf die 
                                            # Objektvariable self.name = name
                                            # aus der __init__

# AUf Geschütze Objektvariable zugreifen __stärke
    def get_stärke(self):
        return self.__stärke


if __name__ =="__main__":
# Ein pokemon Objekt = bisasam, instanziert = Aufruf der Klasse mit übergabe 
# Parameter, self muss nicht mit übergeben werde, passiert automatisch 
    bisasam = Pokemon("Bisasam", 0, 2) # bisasam wird Instanziiert


    schiggy = Pokemon("schiggy", 5, 1) # Schiggy wird Instanziiert
   

    print(bisasam.get_stärke)       # greifen auf dei get_stärke Methode zu
                                    # um  die geschützte Variabele wieder sichtbar zu machen


    
# ------------   Pokémon Teil 2 ------------------#

class Pokemon:

    def __init__(self, name,):
        self.__name = name
        self.__lebenspunkte = 42
        self.__level = 1

    def vorstellen(self):
        print(f'{self.__name}, {self.__name}!')

    def zeige_lebenspunkte(self):
        return self.__lebenspunkte

    def zeige_level(self):
        print(f'{self.__name} :: {self.__level}')

    def level_up(self):
        self.__level += 1

    def attackieren(self, other, schaden):
        other.__lebenspunkte -= schaden

            

if __name__ == '__main__':
    p1 = Pokemon("Pikaschu")
    p2 = Pokemon("Schiggy")

p1.level_up()
p1.zeige_level()
p2.zeige_level()

p1.attackieren(p2, 10)  # p1 greift p2 mit 10 schadenspunkten an 
print(p2.zeige_lebenspunkte())



# ------------------ Magische Methoden ------------------------  #
#https://developer-akademie.teachable.com/courses/python-grundlagen/lectures/48824510

# Magische Methoden werden vom Interpreter automatisch in bestimmten Kontext aufgeruffen.

#                   Liste der Magischen Methoden
#   Operatoren           Mgische Methode       Benötigte Parameter
#       +             __add__(self, other)           self,other               
#       -             __sub__(self, other)           self,other   
#       *             __mul__(self, other)           self,other   
#       /             __trueediv__(self, other)      self,other   
#      ==             __eq__(self, other)            self,other   
#       <             __lt__(self, other)            self,other
#       >             __gt__(self.other)             self,other


class Pokemon:

#   Magiische Methode
    def __init__(self, name,):
        self.__name = name
        self.__lebenspunkte = 42
        self.__level = 1

#   Magiische String Methode
# Wofür wird die Funktion __str__ bei Objekten verwendet?
# Um eine Textuelle Darstellung des Objekts zu erstellen, die mit der Funktion print() angezeigt werden kann.
    def __str__(self):
        return f"Name: {self.__name}\nLebenspunkte: {self.__lebenspunkte}\nLevel:{self.__level}"

#   Magiische >als Methode
# Wofür wird die Funktion __gt__ bei Objekten verwendet?
# Um zu Prüfen, ob ein Objekt größer als ein anderes ist
    def __gt__(self, other):
        return self.__level > other.__level

#    Methode    
    def vorstellen(self):
        print(f'{self.__name}, {self.__name}!')

    def zeige_lebenspunkte(self):
        return self.__lebenspunkte

    def zeige_level(self):
        print(f'{self.__name} :: {self.__level}')

    def level_up(self):
        self.__level += 1

    def attackieren(self, other, schaden):
        other.__lebenspunkte -= schaden

            

if __name__ == '__main__':
    p1 = Pokemon("Pikaschu")
    p2 = Pokemon("Schiggy")

    p1.level_up()
    p2.attackieren(p1, 5)

    print(p1)
    print(p2)

#  bezieht sich auf die Magische Mthode > als __gt__
    print(p1 > p2)      # Aufruf brauch nur das > zeichen



# ----------------   Funktionen vs. Methoden ----------------#

#Methode
# Wenn ich von einer Classe spreche, also einer Beschreibung wie ein Objekt später zusammengebaut wird. 
# Habe ich immer Objekt Variablen und Methoden.
# Eine Mthode gehört immer zu einem Objekt. 
# Zum aufruffen einer Methode brauch man immer ein Objekt
# Bei jeder methode ist der erste übergabe Parameter die Self Instanz.
# Self bezieht sich auf das Objekt selber.
 

class Pokemnon:

    def __init__(self, name):
        self.name = name
        self.lebenspunkte = 42
        self.level = 1

#   Methode wird definiert
    def vorstellen(self):       
        print(f'{self.name}, {self.name}!! ')

bisasam = Pokemon("Bisasam")
bisasam.vorstellen()    # benötigt kein Parameter self, da sich dies schon auf 
                        # das Objekt selbst bezieht , bisasam



#Funktion
# Funktionen werden nicht auf Objekte aufgerufen. hat keine self instanz

# Worum handelt es sich bei len() in Python?
# Eine Funktion, die die Länge eines iterierbaren Objekts zurückgibt



# ---------------   try und except  -----------------------------#
# try und except ist dafür da um Laufzeit Fehler ab zu fangen

# try:
#   <Anweisung 1>
#
#   ...
#
#   <Anweisung n>
#
#except <Exceptiontyp>:
#   <Fehlerbehandlung>
#
#finally:
# <Wird auf jeden Fall ausgeführt!>
liste = [1, 2, 3, "Flo", "Junus", "Pascal"]

try:
    index = int(input("Bitte gib einen Index ein: "))
    liste[index]
except IndexError as ex:    # fängt Index Errors ab 
    print(f"Der Zugriff ist FEhlgeschlagen.\n{ex}")
except ValueError:  # fängt nur ValueErrors ab 
    print("bitte gib eine Zahl ein!") 
except Exception as ex:   # fängt alle fehler ab 
    print(f"Es ist ein Fehler aufgetreten. \n{ex}")
finally:
    print("Ich bin fertig!")



try: 
    f = open("test.text", "w")
    f.wirte("Hallo Welt!")
except Exception:
    pass
finally:
    f.close