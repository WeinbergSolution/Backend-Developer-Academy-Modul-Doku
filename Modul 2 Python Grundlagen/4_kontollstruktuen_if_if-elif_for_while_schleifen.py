#---------------- Kontrollstrukturen

# ---------  if-Anweisungen (Wenn dann mach das(if) ... sonst das (else) ....)
# if Bedingung:
#    Anweisung 1
#    Anweisung 2
#    .....
#    Anweisung n

passwort = input("Gib dein Password ein: ")

if passwort == "abc123":
    print("Das Passwort ist korrekt!")
else:
    print("Das Passwort ist falsch! ")



#---------  if-elif-else-Anweisungen \ Entspicht elseif in JS

note = input("Gib die Note ein: ")

if note == "1":
    print("Du bist der Beste ")
elif note == "2":
    print("Zwei nicht schlecht mein bester! ")
elif note == "3":
    print("Mittel Maß, da geht mehr! ")
elif note == "4":
    print("Digga eine 4, geb mehr Gas! ")
elif note == "5":
    print("Uff eine 5, vorletzer zu sein macht doch keine Freude! Nachsitzen!")
else: 
    print("Mit einer 6 bist du hier Fehl am Platz! ")



#--------------   match-case \ Pondong zu Switch Case in JS
# match-case sind ein mächtiges Werkzeug, das über switch-case hinausgeht!
# Datenstrukturen oder Objekte können auch der Parameter sein
#z.b. eine liste [1,2,3]
#Es wird geprüft ob die Variable das definierte Objekt beinhaltet.


match note:
    case "1":
        print("sehr gut!")
    case "2":
        print("gut!")
    case "3":
        print("Befriedigend.")
    case "4":
        print("Ausreichend!")
    case "5":
        print("Mangelhaft!")
    case "6":
        print("Ungenügend!!!")
    case _:
        print("Geben sie eine gültiege Note von 1 - 6 ein!")




#---------------   for-Schleifen ----------------
# wird verwendet, wenn ein vorgegebener Bereich durchlaufen werden soll. z.n eine Datenstrucktur, eine Tuple, ein Dictionary. 
# Sie endet, wenn das ende der Datenstruktur erreichtr wurde
# Wird verwendet, wenn der Durchlauf des vorgegebenen Bereichs nicht durch den Benutzer unterbrochen werden soll. 
# Endet, sobald der vorgegebene Bereich vollständig durchlaufen wurde. Die Bedingungen wäre hier "so lange nich nicht am Ende angekommen".
# kann nicht endlos laufen. 

# Beispiel: Listen, Tupel, Strings, Zahlenbereiche, ...

# Forschleifen in Python sind interator basiert und lkesen sich wie eine Geschichte

#Beispiel: Für jedes Passwort in der Liste passwörter, 
#Gebe das passwort aus, ist die Länge kleiner als 5 brech abaus der Schleife aus.

passwörter = ["abc123", "gehe1m", "test", "123456"]

for passwort in passwörter:
    print(passwort)     # gibt alle passwörter unter einadner aus
    if len(passwort) <5: # definiert die Abbruchbeding
        break           # break löst den Abbruch der schleife aus.





# -------------   while-Schleifen ----------------------------
# Eine While Schleife wird verwendet, wenn kein vorgegebener Bereich durchlaufen werden soll, sondern der Abbruch von einer Bedding abhängt
# Wird verwendet wenn der Benutzer den Abbruch der Schleife steuern können soll.
# Endet, sobald die Bedingung nicht mehr erfüllt ist.
# Kann endlos laufen 
#Beipiel: Hauptereignesschleife, Videospiele, Client-/ServerProgrammierung, ...

# Besipiel while Bedingung :

x = 25                          # definierte Variable
runde = 1                       # definiter Iterationsschritt oft i

while x > 0:
    print(f"Runde: {runde}")
    runde += 1                  # inkrementiert runde      
    x -= 1                      # dekrementiert x


# Weitere Beispiel:

name = input("Gin einen Namen ein ! X zum Abbruch: ")
namensliste = []

while name != "X":
    namensliste.append(name)   # name wird der Namenslise mit append hinzugefügt
    print(namensliste)
    name = input("Gin einen Namen ein ! X zum Abbruch: ")





# -----------------   Endlosschleifen ---------------------
# Endlosschleifen werden oft While True schleifen genannt, da man aus der 
# schleife nicht ausgebrochen werden kann da die Bedingung immer True ist.
# Endlos schleifen werden häufig verwendet für:
# Als Hauptereignesschleife in Videospilen
# In der Netzwerkprogrammierung bei der Bereitstellung eines Servers

teilnehmerliste = []

teilnehmer = input("Bitte gib einen Teilnehmer ein (X): ")

while teilnehmer != "X":   # teilnehmer != "X" könnte durch True ersetzt werden 
    teilnehmerliste.append(teilnehmer)
    teilnehmer = input("Bitte gib einen Teilnehmer ein (X): ")

print(teilnehmerliste)         # dieser befehl wird nie mals erreicht





# ------------   while-Schleifen vs. for-Schleifen ----------

#while-schleife

# Eine While Schleife wird verwendet, wenn kein vorgegebener Bereich durchlaufen werden soll, sondern der Abbruch von einer Bedding abhängt
# Wird verwendet wenn der Benutzer den Abbruch der Schleife steuern können soll.
# Endet, sobald die Bedingung nicht mehr erfüllt ist.
# Kann endlos laufen 
#Beipiel: Hauptereignesschleife, Videospiele, Client-/ServerProgrammierung, ...

#for-schleife

# wird verwendet, wenn ein vorgegebener Bereich durchlaufen werden soll. z.n eine Datenstrucktur, eine Tuple, ein Dictionary. 
# Sie endet, wenn das ende der Datenstruktur erreichtr wurde
# Wird verwendet, wenn der Durchlauf des vorgegebenen Bereichs nicht durch den Benutzer unterbrochen werden soll. 
# Endet, sobald der vorgegebene Bereich vollständig durchlaufen wurde. Die Bedingungen wäre hier "so lange nich nicht am Ende angekommen".
# kann nicht endlos laufen. 
# Beispiel: Listen, Tupel, Strings, Zahlenbereiche, ...





#-----------------   Walross-Operator ":=" --------------------
# In dem Beipiel: wird gegen das Dry = Dont repeat your self priziep verstossen 
# Fügt eine Zuweisung und eine Abfrage gleichzeiotig aus
# Der Walross-Operator verbessert die Lesbarkeit und das Intuitive schreiben von Code

teilnehmerliste = []

teilnehmer = input("Bitte gib einen Teilnehmer ein (X): ")

while teilnehmer != "X":   
    teilnehmerliste.append(teilnehmer)
    teilnehmer = input("Bitte gib einen Teilnehmer ein (X): ") # DRY verstos

print(teilnehmerliste)           


# BEssere lösung ohne Dry Verstos mit dem Walross-Operator :=
# Mit dem Walross.Operator kannst dui einer Variable einben Wert zuweisen und diese dann für eine Bedingungsprüfung verwenden.

teilnehmerliste = []



while (teilnehmer := input("Bitte gib einen Teilnehmer ein (X): ")) != "X":
    #   Teilnehmer wird mit dem Walross-Operator die variable "X" zugewiesen und als Abbruch bedingung hinterlegt ohne ein 
    # erneuten Input abfrage zu verlangen
    teilnehmerliste.append(teilnehmer)
    

print(teilnehmerliste)  
   

