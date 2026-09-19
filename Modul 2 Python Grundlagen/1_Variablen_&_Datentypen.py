#https://developer-akademie.teachable.com/courses/python-grundlagen/lectures/48368139

#String:
name = "Florian"

#Integer nur ganze Zahlen
alter = 42
# _ ist nur für die lesbarkeit, Python ignoriert das
guthaben = 100_000 

#Float
gewicht = 76.5

#Boolen / Warheitswert 
#  True wird als 1 interpetiert False als 0 oder 0.0 alles über 0.1 ist True 
# leerer string "" = True  
#gefüllter string "." odere "0" = FALSE
anwort = True / False

# Datentyp abfragen type()

# Beispiel:
print(type(name))

# Datentyp Umwandeln
str() # wert in einen STring umwandeln
int() # String in integer umwandeln
float() # Zahl oder Stirng in Float Umwandeln
bool() # Zahl oder Zeichenkette in True or Fals umwandeln



# Übunsaufgaben Datentypen 
print(int(42.5))        # Ergebis 42
print(float(-1))        # -1.0
print(str(0.5))         # "0.5"
print(bool(0.001))      # True
print(str("False"))     # "False" / unnötig
print(int(False))       # 0
print(float("10"))      # 10.0
print(bool('0'))        # True / leerer String = FAlse
print(int("False"))     # Fehler = Value Error / int sucht nach zahlen im string
print(float("True"))    # Fehler = Value Error