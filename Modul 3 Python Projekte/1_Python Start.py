#### -----------------------Python Start----------------------####

##---------------  01 - Virtuell Enviroment  -------------##

# Eine Virtuelleumgebung ist ein Projekt in eigenen Ordner
# Das hat den Vorteil das die abhängikeiten und Deependencies nur für und von diesem Projekt sind.

# Zum einrichten einer Virtuelen Pythen Umgebung benutze Folgenden Befehl

#Schrit 1:
# Neuen Projekt Ordner Anlegen

#Schrit 2:
# Aus dem Projektverzeichnis in der Console eingeben:
# hier gibt es 3 Varianten
# python -m venv
# python -m env
# python -m venv .venv      "best Praktis"
 
#Schrit 3:
# .venv Aktivieren

# ".venv/Scripts/activate"      / cmd
# .\.venv\Scripts\Activate.ps1  / powershell





##------------------    02 - .env Datei  ----------------##

# Schrit 4:
# .env Datei im projektordner erzeugen

# Hier kommen und gehören sensible Daten rein!
# Account informationen, Secret Key, Passwörter

#Schrit 5:
# main.py im Projektordner erzeugen.
# Hier kommt das Haupt Script des Projects rein.

#Schrit 6:
# Damit man mit der main.py arbeiten kann, müssen wir
# python-dotenv über pip install installieren 
# Dadurch wird unter dem Ordner site-packages der Dotenv Ordner erzeugt.

#pip install python-dotenv

#schrit 7:
# In der main.py importieren wir jetzt folgende Dinge

#importiert die load_dotenv from dotenv
#Befehl:
#from dotenv import load_dotenv  

# Importiert Das Operating System 
# Befehl:  
# import os     

# Läd die .env
# Befehl:  
# load_dotenv()  

# SECRET_KEY aus der .env in die main.py holen
secretkey = os.getenv("SECRET_KEY") # läd den SECRET_KEY aud der .env
                                    # und speichert ihn in "secretkey"

print(secretkey)                    # gibt den secretkey auf der console aus.
                                    # nur Demo, macht man so nicht.


#Schrit 8:
# Wird das Projekt nicht mehr benötigt, Ordner löschen.



##------------------      03 - pip freeze  ----------------##

# Befehl: pip freeze
# Mit pip freeze wir ausgegebn welche Dependecies sprich abhängigkeiten notwendig sind um das Programm aus zu führen.

# Befehl: pip freeze > requirements.txt
# Mit pip freeze > requirements.txt wird eine .txt der Abhängikeiten erzeugt.Diese wird im Prijektornder abgelegt.



##------------------  04 - Gitignore in Python  ----------------##

# Die gitignor datei ist dafür da, zu definieren, was nicht mit auf Git oder Github geladen wird.

# .gitignor
# Die .gitignor wird im Projektornder angelegt.

# Standart gitignore:

# --- Python ---
__pycache__\
*.py[cod]
*.pyo
*.pyd
*.pkl
*.log

# --- Virtuelle Umgebung ---

venv/
env/
.venv/
.env

# --- Distribution / Packaging ---
build/
dist/
*.eggs/

# --- Test / Coverage ---
.Coverage
htmlcov/
.tox/
.pytest_cache/

# --- IDE / Editor ---
# idea kommt bspw. von Webstorm
.vscode/
.idea/
*.swp
*.swo

# --- System Files ---
.DS_STORE
Thumbs.db


##----------------  04 - README.md  ----------------##

# Die README.md wird in jemden Projekt angelegt.
# Sie ist für die Beschreibung des Projekts.
# Wenn man neue Sachen hinzufügts oder eionen neuen Prozess,Projekt Startet,Neue Features, dies direkt in der README.md eintragen.



##---------------- Bonus- init.py  ----------------##

# Erzeuge den Ordner "helper" im Hauptverzeichnis des Projekts
# Dort erzeugen wir fürs Beispiel eine "math.py"

# Um die math.py jetzt in der main.py verwenden zu können,
# improtieren wir diese.

# Befehl:
# import helper.math as mathHelp

# nicht zuende gesehn Link:
#https://developer-akademie.teachable.com/courses/python-grundlagen3/lectures/63241814