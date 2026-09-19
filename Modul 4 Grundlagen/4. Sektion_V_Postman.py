### -------------------- Backend Modul 4 ----------------------------- ###

## ------------ Sektion V - Postman --------------------##

          # ----------     Einleitung Postman    -------- #


 #---------   01 - GitHub API Vorstellung -----------#

# Link : https://docs.github.com/de/rest?apiVersion=2026-03-10

# 1. Öffne die Github rest API Doku
# 2. Wähle schnellstart.
# 3. Wähle Curl aus. 
#     in Vielen Dokus wird nur curl angeboten, daher verwenden wir hier auch curl

#     curl --request GET \ 
#         (definiert die anfrage)
#     --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \ 
#         (welche URL fragen wir an )
#     --header "Accept: application/vnd.github+json" \ 
#         (definiert den content-type)
#     --header "Authorization: Bearer YOUR-TOKEN"
#         (gibtz die Authoriesierung mit)

#     Die Curl version auf dem System, wenn installiert können wir mit 
#         curl --version 
#     abruffen.



# ------------- 02 - Collection einrichten --------- #

# Wenn wir wissen, das wir eine collection anlegen wollen, machen wir das idealter weiße vor dem ersten Request. 

# 1. Links im menü auf collections klicken 
# 2. auf das + symbol gehn und blank collection ausswählen
# 3. Name der collection zuweisen
# 4. ersten neuen request erstelln und diese über den save butten der collection hinzufügen. 



# -------   03 - Collection Variablen -------#

# Aufbau der Collection

# overview:
#     Dort kann man Notizen und Informationen zu der Collection speichern 

# Authorization:  
#     Hier kann man Grundlegende Autorisierungen für die Collection anlegen. 

# Scripts:

# Variables:
#     Hier können Variablen defioniert werden für die Collection, die immer     
#     wider verwendet werden können. Z.b. die Base URL
#     Möchte man eine Variable verwenden wird sie in zwei curly brackets
#     definiert {{BASE_URL}}, diese muss natürlich zuvor in der Collection 
#     unter Variables angelegt worden sein.
       

# Runs:


# -------   04 - PAT generieren --------- #

# PAT = Personal Access Token

# Den PAT generiern wir in unserem GitHub Profiel, folgendermaßen.

# 1. klicke auf dein logo rechts oben in der Ecke und wähle Settings.
# 2. In den Settings wählt man Developer Settings aus.
# 3. Dort erzeugen wir einen Fine-frading token.
# 4 Erlaube volgende Repositories Permissions:
#     Actions Read and Write
#     Administration Read and Write
#     Issues Read and Write
#     Pull requests Read and Write
#  Account permissions:
#     Profile Read and Write
# 6. Token Generieren.
# 7. Generierten Token in die GitHub Collection in Postman als Variable speichern.



# ---------   05 - User abfragen ----------- #

# Doku :
# https://docs.github.com/en/rest/users/users?apiVersion=2026-03-10#list-users

# Wie rufe ich mit der Github Collection in Postman jetzt einen User ab, bzw. meinen User, für die ich die Authoriesierung habe. 

# gesamte API URL
#     https://api.github.com/users/USERNAME

# Wir brauchen aber nur den part: 
#     /users/USERNAME
#     da die Base URL schon als BASE_URL hinterlegt ist.

# Dies ruft alle öffentlich zugängliche Profiel daten ab, man benötigt keine Authentication.

# Meine eigenen Profiel informationen rufe ich folgendermaßen ab. 
#     {{BASE_URL}}/user
#     Dazu benötiegen wir einen Authorization Key den wir unter dem Header anlegen.
#     Trage dort Als 
#         Key: Authorization 
#         Value: Bearer {{GitHubPAT}}
#         GitHubPAT muss natürlich in der Collection unter Variablen gesetzt sein. 



# --------------   06 - GET Repo -------------------- #

# Öffentliche Repos abrufen ohne Authentication
#     {{BASE_URL}}/users/WeinbergSolution/repos

# Alle Nutzer speziefischen Repos abruffen mit Authentication, wo im header der Authentication Key & Value gesetzt wurde.
#     {{BASE_URL}}/user/repos



# -----------------   07 - Pagination Params API Prameter  --------------------#

# Doku:
# https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2026-03-10

# Filter setzen um Öffentliche und oder Private Repos zu filtern.
# Denn die API begrentzt Ausgaben auf 30 issues also Einträge.

# Hier wird der Key Value Pair ?page=1 interessant.
#     Dies sagt aus wie viele seiten angezeigt werden sollen in dem fall 2 

# DEsweiteren ist der Zustz per_page=100 interessant, da man damit angibt wie viele einträge auf einer seite vorkommen sollen. 

# gesamter Request: 
#     {{BASE_URL}}/user/repos?page=1&per_page=100

# Params also eingrenzungen der API abfrage beginnen immer mit einem ?
#     {{BASE_URL}}/user/repos?page=1&per_page=100

# Möchte ich mehr als ein Parameter setzten hänge ich ein & ran
#     z.b.: &per_page=100



# ----------- 08 - GET Issues -------------------- #

# Doku: 
# https://docs.github.com/en/rest/issues/issues?apiVersion=2026-03-10

# Neuen Ordner anlegen in Postman unter Github COllections für die Issues abfragen
#     Neues verzeichnis : Issues

# Neuer Request anlegen : 
# Issues abrufen über Postman 
#     {{BASE_URL}}/repos/WeinbergSolution/portfolio/issues


# ---------------   09 - POST Issues  --------------#

# Um ein Issue über Postman hinzuzufügen benötiegen wir jetzt einen 
#     POST Request
#     {{BASE_URL}}/repos/WeinbergSolution/portfolio/issues

# Desweiteren müssen wir den Body des Post Requests anpassen.
#     raw auswählen.

# Wir benötiegen einen Titel und einen Body z.b.:
#     {
#     "title":"test2",
#     "body":"dies ist ein issue Post Request aus Postman heraus, für ein Test!"
#      }

# Desweiteren wird eine Authoriesierung benötigt im Header des Post Request.
#     Key: Authorization
#     Value: Bearer {{GitHubPAT}} 
#                     (GitHubPAT muss natürlich in der Collection als Variable angelegt sein!)



# ------------------   10 - PATCH Issues  -------------------#

# Ein Issue kann mit einen PATCH Request über Postman geändert werden. 

# Die Reguest URL bleibt fast identisch wie bei einem POST nur benötiegen wir die ID also den geneauen Issue den wir PATCHEN wollen
#     POST URL: 
#         {{BASE_URL}}/repos/WeinbergSolution/portfolio/issues
#     PATCH URL: 
#         {{BASE_URL}}/repos/WeinbergSolution/portfolio/issues/2
#             Die 2 steht für den 2 Issue in dem portfolio Repo



# ----------------   11 - CRUD mit Assignees ----------------- #

# Doku: 
# https://docs.github.com/de/rest/issues/assignees?apiVersion=2026-03-10#list-assignees

# POST Request für einen assignee
#     {{BASE_URL}}/repos/WeinbergSolution/portfolio/issues/1/assignees
#         Body anpassen : 
#             {
#                 "assignees":["WeinbergSolution"]
#             }
# DELETE Request um ihn wieder zu löschen 
#     {{BASE_URL}}/repos/WeinbergSolution/portfolio/issues/1/assignees