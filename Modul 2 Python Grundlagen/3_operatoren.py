# ------------   Arithmetische Operatoren und deren Rangfolge
  
# <Operad 1>      <Operator>       <Opernad 2>          name
#    10                 **               2          Potenz Operator
#-----------------------------------------------------------------------
#    42                 *               30
#    30                 /               15    
#    80                 //              40        Integer Division Operator 
#    42                 %               12             Modulo Operator   
#------------------------------------------------------------------------
#    12                 +               10
#    20                 -               11

  




# Beim Dividieren mit einem / kommt immer ein Float raus 
print(30/15)            # = 2.0

# Integr Division benötigt // dann kommt ein Integer raus
print(30//15)           # = 2

#Wichtig in der Integer Divison werden nur die Zahlen vor dem Komma angzeigt, es wird nicht gerundet, das kann zu fehlern führen
print(7//2)           # = 3
print(5//6)           # = 0

# Der Modulo Operator % gibt immer den rest aus, geht die division auf und es gibt kein rest kommt 0 raus. 
print(42 % 12)        # = 6
print(10 % 3)         # = 1

# Potenz Operator **
#Tip: 2 Potenzen bis 10 asuwendig lernen. 
print(2**5)           # = 


# Operatoren Rangfolge Beispiele: 
print(5**3 + 2)            # = 127
print(4 + 3 - 5)           # = 2
print(6 + 8 / 2)           # = 10.0
print(10 * 2**3)           # = 80
print(5 * 9 * 2 / 10)      # = 9.0
print(5 % 3 * 7)           # = 14
print(6 % 5 + 3)           # = 4
print(10 % 2**2)           # = 2

# Operator rangfolge ändern () haebn die hächste Bindugsstäreke
print((6 + 8) / 2)           # = 7.0

 

#------------------------  Übungsaufgaben Arithmetische Operatoren

print(12 * 12)                  # = 144
print(2.5 + 3.5)                # = 6.0
print(20 / 5)                   # = 4.0
print(15 – 3 * 5)               # = 0
print(8 + 10//4)                # = 10
print(8 + 10/4)                 # = 10.5
print(20 / (5 – 4))             # = 20.0
print(4 * 2.5 / 4)              # = 2.5
print(1//2 - 3//4)              # = 0
print((12 % 5) * (5 % 12))      # = 10
print(2**3)                     # = 8
print(4**(8 - 5))               # = 64
print(2**(8 // 2))              # = 16
print(5**2 * 3)                 # = 75
print((8 - 5)**(27 // 9))       # = 27
print("apfel" + "baum")         # = "apfelbaum"
print(5 * ("a" + "b"))          # ="ababababab"
print("x" * 2**3)               # = "xxxxxxxx"
print(12 % 5)                   # = 2
print(42 % 43)                  # = 42
print(2**10 % 2)                # = 0
print(5 * 4 * 3 * 2 * 1.0)      # = 120.0
print(0 * "Florian")            # = ""
print("xyz" * (12 % 5))         # = "xyzxyz"



#--------------------  Inkrement- und Dekrement-Operator (i++ und i--)

# Inkrementieren in Python i++ = +=
i = 0 
i += 1              # ist das gleiche wie i = i + 1

# Dekrementieren in Python i-- = -=
i = 0 
i -= 1              # ist das gleiche wie i = i - 1


#--------------------- Operatoren schnell schreibweise 
i = 5

# i = i /2
i /= 2
i //= 0

a = 5
a **= 2

b = 10
b %= 3



#------------- Vergleichsoperatoren Rangfolge ist gleich (von links nach rechts)

# Vergleichsoperatoren geben einen bool zurück =  True or False 

# <Operad 1>      <Operator>       <Opernad 2>          name
#   12                  <               15           kleiner als
#   20                  <=              22           kleiner als oder ist gleich
#   56                  ==              56           gleich
#   17                  !=              42           ungleich
#   18                  >=              18           größer als oder ist gleich
#   99                  >               33           größer als


a = 2
b = 3
print(a < b)            # = True
print(a <= b)           # = True
print(a == b)           # = False
print(a != b)           # = True
print(a > b)            # = False
print(a >= b)           # = False

# Vergleichsoperatoren sind Case sensetiv
c = "Pascal"
d = "pascal"
print(c == d)           # = False \ Case sensetiv
print(c != d)           # = True
print(c < d)            # = False \ vergleicht die länge
print(c <= d)           # = True  \ vergleicht die länge




#------------  Logische Operatoren ----+ Rangvolge / Bindungsstärke

# <Operad 1>      <Operator>       <Opernad 2>          name
#                   not
#                   and                               AND Operator
#                   or                                Or Operator

# x or ist ein für die Bitweise Kombitation zustädnig ist

#------------- binärer Operator

#                   ^                                x Or Verknüpfung


# Der x or Operator ^ bietet sich super zur verschlüsselung an, der Verschlüsselte Klartext lässt sich mit dem Schlüssel und mit dem x or 
# Operator wieder decodieren

# 10101 <- klartext
# 11011 <- Schlüssel ^
# --------------------
# 01110 <- Verschlüsselter Klartext
# 11011               ^
# --------------------
# 10101



print(2 < 3 and 3 < 5)     # = True \ Beide Bedingung sind richtig 
print(2 < 3 and 3 == 5)     # = False \ Beide Bedingung müssen richtig sein
print(2 < 3 or 3 == 5)     # = True \ Eine der Bedingung muss richtig sein
print(2 < 3 or 3 != 5)     # = True \ Eine der Bedingung muss richtig sein
print((2 < 3) ^ (3 != 5))  # = False \ X or benötigt True und False
print((2 < 3) ^ (3 == 5))  # = Ture \ X or benötigt True und False
print( True or 2 < 3 and False) # = Ture \ erst das And dann das Or Rangfolge
print( True and 2 < 3 and False) # = False \ Rangfolge gleichwertig
print( (True or 2 < 3) and False) # = False \ Operator Rangfolge geaändert ()
print(not (True or 2 < 3 and False) ) # = False
print(True and not False)   # = True \ erst not Operator dann and


# ---------- Alle Operatoren und deren Rangfolge

# <Operand 1>      <Operator>       <Operand 2>          Name / Bedeutung
#    10                **               2                Potenz Operator
#-----------------------------------------------------------------------
#    42                *                30               Multiplikation (mal)
#    30                /                15               Division (geteilt durch)
#    80                //               40               Integer Division Operator 
#    42                %                12               Modulo Operator   
#-----------------------------------------------------------------------
#    12                +                10               Addition (plus)
#    20                -                11               Subtraktion (minus)
#-----------------------------------------------------------------------
#    1                 ^                0                Exklusives ODER (entweder oder)                                            x Or
#-----------------------------------------------------------------------
#    5                 <                10               kleiner als
#    5                 <=               10               kleiner als oder gleich
#    5                 ==               5                gleich
#    5                 !=               10               ungleich
#    10                >=               5                größer als oder gleich
#    10                >                5                größer als
#-----------------------------------------------------------------------
#                      not              True             Logisches NICHT (nicht)
#-----------------------------------------------------------------------
#    True              and              False            Logisches UND (und)
#-----------------------------------------------------------------------

#    True              or               False            Logisches ODER (oder)




# --------------   Übungsaufgaben Logische Operatoren

# Aufgabe 1:
# Welche Wahrheitswerte kommen bei den folgenden logischen Ausdrücken heraus?
print(True and False and True or False)         # = False
print(not False or not True)                    # = True
print(True and (False or not False))            # = True
print(not (not False ^ True or not False))      # = False
print(True and False ^ True and False)          # = False

# Aufgabe 2:
# Worin besteht der Unterschied zwischen den beiden Operatoren ^ und or?
#  Or etweder die eine oder die andere oder beides
# ^ x or entweder das eine oder das andere beides geht nicht 


# Aufgabe 3:
# Welche Wahrheitswerte kommen als Ergebnis heraus?
print(2 < 3 and not 2 > 5)                      # = True
print(not True ^ False or 3 == 2 + 1)           # = True
print(not not not 2 % 5 == 7 % 5)               # = False
print(True and False ^ True and False)          # = False
print(True ^ False ^ 0 ^ 1 ^ (2 > 3))           # = 0
# Achtung vergleicht man das x Or als Binöroperator mit einer Zahl un einem Boolen, kommt eine Zahl raus. 


# --------------  Beispiele zu den Operatoren und Operatorrangfolgen

a = 2.5
b = -5
c = 20
d = "Hallo"
e = "Python"

print(d + " " + e)              # = "Hallo Python"
print(c % 7)                    # = 6
print(16** (a - 2))             # = 4.0 \ Potenziere ich mit 0.5 = Wurzelziehn
print(d**c)                     # = TypeError Stings werden nicht Potenziert
print((b + c) / b)              # = -3.0
print(20** (2 * a + b))         # = 1.0 \ 
print(2 * a * d)                # = TypeError \ Strings * float nicht möglich 
print((c - b) // 7)             # =  3 \ -- ergibt plus
print(e // "Python")         # = TypeError / & // funktioniert nicht bei Strings
print(b**2 - 25)                # = 0
print(True or False ^ True)     # = True
print(0 < 1 and True ^ True)    # = False