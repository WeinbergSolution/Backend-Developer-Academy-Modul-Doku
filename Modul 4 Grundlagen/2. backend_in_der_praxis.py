### -------------------- Backend Modul 4 ----------------------------- ###

## ------------ Backend in der Praxis: To-Do Liste --------------------##

# ----------     01 - Trennung von Backend und Frontend    -------- #

#     Forntend     ------------------->   Backend 
#   HTML, JS, CSS                          Linux
#     Frontend    <--------------------   Backend
#                     Fetch Befehl
                           

# Fügen wir z.b neue To Does, hinzu, werden sie an das Backend gesendet, wo diese auf dem Server verarbeitet werden. 
# Fragen wir diese To Does wieder ab, geschieht das mit einem Fetch Befehl. 



# ----------     02 - Todo-Frontend anlegen    -------- #

# 1. Neuen Ordner anlegen "Todoliste"
# 2. in dem Projektordner jeweils einen "todo_forntend" & "todo_backend" Ordner anlegen.
# 3. todo_frontend verzeichnes mit vs conde öffnen. 
# 4. im todo_frontend verzeichnis "index.html" anlegen.

# <!doctype html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Document</title>
#   </head>

#   <body onload="render()">
#     <h1>Todo-Liste</h1>
#     <form
#       onsubmit="
#         addTodo();
#         return false;
#       "
#     >
#       <input type="text" placeholder="Neues Todo" id="todoinput" />
#       <button>hinzufügen</button>
#     </form>

#     <ul id="todoList"></ul>

#     <script>
#       let todos = ["Einkaufen"];
#       function addTodo() {
#         let todoText = document.getElementById("todoinput").value;
#         todos.push(todoText);
#         document.getElementById("todoinput").value = "";
#         save();
#         render();
#       }
#       function save() {
#         fetch("http://127.0.0.1/todoes", {
#           body: JSON.stringify(todos),
#           method: "POST",
#         });
#       }

#       function render() {
#         todoList.innerHTML = "";
#         todos.forEach((todo) => (todoList.innerHTML += `<li>${todo}</li>`));
#       }
#     </script>
#   </body>
# </html>



# --------------- 03 - Backend erstellen mit JSON-Server ----------- #

# Backend anlegen

# 1. Öffne das Backend verzeichnis. 
# 2. Öffne es den Pfad in vs Code.
# 3. Prüfe ob Node.js intsalliert ist npm --version
# 4. JSON Server installieren 
#   npm install -g json-server
# 5. File anlegen als Datenbank "db.json" und testweiße befüllen
# {
#     "todos": [
#         {
#             "id": 1,
#             "title": "obst kaufen"
#         },
#         {
#             "id": 2,
#             "title": "Milch kaufen"
#         }
#     ]
# }
# 6. JSNON Server Starten 
#   json-server --watch db.json
# 7. über die URL http://localhost:3000/todos lässt sich das Backend abrufen 



# ----------   04 - Todos laden und rendern ------------ #

# Neue funktion im Frontend anlegen die, die Daten aus dem Backend Fatcht.

# async function loadTodos() {
#         const url = "http://localhost:3000/todos";
#         let resp = await fetch(url);
#         todos = await resp.json();
#         render();
#       }

# dazu den onload auf den Body ändern. 
# <body onload="loadTodos()">


# -----------   05 - Todos posten  ------------------- #

# -----------   06 - Content-Type Header  ------------------- #

# Content-Type auf JSON ändern.

# application/java-archive
#  application/EDI-X12   
#  application/EDIFACT   
#  application/javascript (obsolete) 
#  application/octet-stream   
#  application/ogg   
#  application/pdf  
#  application/xhtml+xml   
#  application/x-shockwave-flash    
#  application/json  
#  application/ld+json  
#  application/xml   
#  application/zip  
#  application/x-www-form-urlencoded  

# function addToServer(todoText) {
#         fetch("http://127.0.0.1:3000/todos", {
#           method: "POST",
#           headers: {
#             "Content-Type": "application/json",
#           },
#           body: JSON.stringify({
#             title: todoText,
#           }),
#         });
#       }


# -------------    07 - So geht es weiter ------------#
