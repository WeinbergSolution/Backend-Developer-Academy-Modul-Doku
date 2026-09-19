#https://developer-akademie.teachable.com/courses/python-grundlagen/lectures/48370185

# Indivudeulle Text ausgabe vom Layout durch """ Anführungszeichen 
#Beispiel: print("""sdsdsd    sdsd  wsdsdsd s)

# länge auslesen aus einem String 
# len()
#Beispiel:
name = "Pascal"
print(len(name)) # = 6

# Ausgabe einzelner Zeichen oder Bereiche eines Strings oder Zahl mit
# [] = die den Index darstellt, postiver index startet die suche von Links,
#  dem anfang des Strings, Negativer Index [-3] startet suche vom ende des String
#psotive Index suche 
print("Pascal"[3])

#negative Index suche 
print("Pascal"[-3])



#------------- slicing
#https://developer-akademie.teachable.com/courses/python-grundlagen/lectures/48370189

#Beispiel: 
print("Pascal"[0:3]) # = "Pas"

#wichtich der Endindex ist exclusiv bedeutet man muss einen Index weiter gehn als man tasächlich extrahieren möchte da die da zwischen 
#liegenden zeichen extrahiert werden


#  Übungsaufgaben Slicing
# Aufgabe 1:
a = "Buchhaltung"
b = "Python ist toll!"

print(a[5])           # = "a"
print(b[-1])          # = "!") 
print(a[:4])          # = "Buch"
print(b[11:16])       # = "toll!"
print(a[-100:100])    # = "Buchhaltung"
print(a[-5])          # = "l"
print(a[-12])         # = Fehler da nur 11 Zeichen
print(a[4:8])         # = "halt"

# Aufgabe 2:
c = "Maximilian"
print(c[:3])  # = "Max"
print(c[:4])  # = "Maxi"
print(c[3:5]) # = "im"
print(c[4:8]) # = "mili"
print(c[7:])  # = "ian"



#----------   Strings konkatenieren = Strings zusammen fügen
 

#https://developer-akademie.teachable.com/courses/python-grundlagen/lectures/48370192

x = "Apfel"
y = "baum"

print(x + y) # = "ApfelBaum"

a = "Hallo"
b = " "
c = "Python"
d = "!"

print(a + b + c + d ) # = "Hallo Python!""

# Strings können nicht Subtrahiert werden. 
# Strings können multipliziert werden 
# Beispiel:
print(d*3) # = !!!
print(3*d) # = !!!


#-----------  Übungsaufgaben Strings konkatenieren

a = "Developer"
b = "Akademie"
c = '.'
d = "com"

print(a + b)                # = "DeveloperAkademie"
print(a + b + c + d)        # = "DeveloperAkademie.com"
print(a + b - b)            # = TypeError unsupported Operand (-)
print(5 * c)                # = "....."
print(3d)                   # = SyntaxError
print(a + d)                # = "Developercom"
print(a + b + d)            # = "DeveloperAkademiecom"
print(d**2)                 # = TypeError unsupported Operand (**)
print(2 * (c + d))          # = ".com.com"
print(3 * c + 2 * d)        # = "...comcom"



# ------------   String-Methoden

# String-Methoden abfragen / auflisten
print(dir(str))

# Metoden werden mit einem . am anfang aufgeruffen und am ende mit einer () abgeschlossen  Bsp: .upper()
# Beispiel:
# Achtung das ist jetzt keine Methode sondern eine Funktion da, da Methode nicht auf ein Objekt angewendet wird.
# .zfill() benötigt einen Parameter = .zfill(10)
print("Pascal".zfill(10)) # = "0000Pascal"

# .upper() schreibt alle Buchstaben Groß. ignoriert Zahlen unhd sonderzeichen und gibt diese normal wieder aus
print("Pascal36!".upper())    # = "PASCAL36!"

# .lower() schribt alle Buchstaben klein. ignoriert Zahlen unhd sonderzeichen und gibt diese normal wieder aus
print("Pascal".lower())       # = "pascal" 

# .capitalize schreibt nur den anfangsbuchtsaben Groß
print("pascal".capitalize())  # = "Pascal"

# .isupper() prüft ob alle Zeichen  Groß geschrieben sind und gibt True or False zurück. Zahlen und Sonderzeichen werden Ignoriert 
print("Pascal".isupper())     # = False

# .islower() prüft ob alle Zeichen klein geschrieben sind und gibt True or False zurück. Zahlen und Sonderzeichen werden Ignoriert 
print("pascal".islower())     # = True

# .isnumeric() Prüft ob nur numerischer werte in String enthalten sind also Zahlen. Es wird True or False zurück gegebn.
print("Pascal".isnumeric())   # = False

# .isalpha() Prüft ob nur Buchstaben im String enthalten sind. Es wird True or False zurück gegebn. Sonderzeichen und Zahlen füren zu False
print("Pascal".isalpha())       # = True

# .split("") Trennt Strings nach einem bestimten Zeichen und speichert die in eine Liste
print("Pascal;Tom;Gustav".split(";"))  # = [ "Pascal", "Tom", "Gustav" ]
print("Pascal;Tom;Gustav".split("."))  # = [ "Pascal;Tom;Gustav" ]

# .splitlines() orientiert sich an Zeilenumbrüchen \n und gibt die Werte in einer Liste aus.
print("Pascal\nTomas\nMia".splitlines()) # = [ "Pascal", "Tomas", "Mia" ]
# gleiches Ergebnis mit .Split("\n")
print("Pascal\nTomas\nMia".split("\n")) # = [ "Pascal", "Tomas", "Mia" ]

# .strip() entfernt alle leer Zeichen am Anfang und Ende eines Strings.
# Achtung: zwischen den Strings wird nix enternt fals leerzeicehn vorhanden da  repalce() verwenden
print("   Pascal   ".strip())       # = "Pascal"

# ..replace() Erstezt Zeichen durch ein neus. Benötigt 2 Parameter. Findes .replace() den Paramter nicht macht es einfach nix.
print("   Pascal   ".replace(" ", ""))  # = "Pascal"

# .count() Zählt wie oft ein Zeichen vorkommt und brauch einen Paramter. Die Methode ist Case sensetiv.
print("Pascal".count("a"))              # = 2         

# .index() Sucht nach einem Devinierten substring oder Zeichen, und gibt den Index zurück an der Stelle wo es das erste mal auftaucht. 
# ein such Parameter wird benötigt. Wird der Paramter nicht gefunden gibt es ein ValueError.
print("Pascal".index("s"))              # = 2
print("Pascal".index("cal"))            # = 3
print("Pascal".index("o"))              # = ValueError substring not Found

# .find() ist wie .index() nur das kein ValueError enstehn kann wenn nicht vorhanden. 
# Ist ein zeicehn nicht vorhanden gibt er -1 zurück den sogenanten Fluchtwert
print("Pascal".find("ol"))              # = -1 Fluchtwert

# in Prüft ob ein Substring oder Zeichen in einem anderen String enthalten ist. Gibt True or False zurück.
print("a" in "Pascal")                  # = True

# String reversen
print("0123456789"[::-1])               # = 9876543210




#------------------------  Übungsaufgaben String-Methoden

#Aufgabe 1: Was wird von dem folgenden Programm ausgegeben?
passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper())                # = "ABC123" 
print(passwort2.lower())                # = "pass wort"
print(passwort3.islower())              # = True
print(passwort2.isupper())              # = False
print(passwort1.zfill(8))               # = "00abc123"
print(passwort2.strip())                # = "Pass Wort"
print(len(passwort3))                   # = 12
print(passwort1.isalpha())              # = False
print(passwort1[3:].isnumeric())        # = True
print("a;b;c;d;e".split(';'))           # = ["a", "b", "c", "d", "e"]
print("01.23.45.67.89".split(';'))      # = ["01.23.45.67.89"]
print(passwort2.replace("Pass",'.'))    # = ". Wort"
print(passwort3.count('3'))             # = 2
print(passwort2.count('s'))             # = 2
print(passwort3.find(2+2))              # = TypeError
print(passwort1.index("4"))             # = IndexError substring not Found


# AUfgabe 2:
#Verwende passende String-Methoden, um die vorgegebenen Strings in die umzuwandeln, die als Kommentar vorgegeben sind:

print("passw0r7".upper())               # = "PASSW0R7"
print("Anime".zfill(11))                # = "000000Anime"
print("florian".capitalize())           # = "Florian"
print("Kaguya".lower())                 # = kaguya
print("0123456789"[::-1])               # = 9876543210
print("0123456789".replace("0123456789", "9876543210"))  # = 9876543210