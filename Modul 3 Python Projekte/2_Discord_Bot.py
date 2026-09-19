### ------------ Discord Bot ------------------ ###

## ------------  01 - Einleitung --------------##

# In dieser sektion werden wir mit Discrod.py arbeiten
# Lernen ein script auszuführen das Permanant läfut
# einen logge zu implementieren von Python der schon vorhanden ist,
# der Permanent mit loggt, was schief läuft. z.b im Debugmodus & dies Permanent Dokumentiert.
# Wir werden mit der Discord py Liberey arbeiten.
# Wie man mit einer großen Dokumentation arbeitet


## -----   02 - Bot erstellen und einladen ----##

# Discord Bots sind wie eigene Acc zu betrachten
# Der Token ist das Passwort.

# Anleitung:
# https://discordpy.readthedocs.io/en/stable/discord.html#discord.Client

# Schrit 1:
# Discord App aufrufen, Server Erstelln

# Schrit 2:
# Im Web auf die Developers Aplication seite navigieren, ides ist der hauptbereich, neue Apolications zu entwerfen. 
# https://discord.com/developers/applications

# Auf der Rechten seite auf App Erstellen klicken
# Name zuweisen, wie die neue Application heißen soll.
# Nutzerbedingungen zustimmen und anhacken. 
# Auf Erstellen Klicken 

# Nach der Erstellung wählen wir aus der Linken Menüleiste den Punkt Bot aus.
# Dort klicken wir auf reset Token, damit ein neuer Token generiert und angezeigt wird. 

# Schrit 3: 
# Unrer dem Menüpunkt "OAuth2" können wir nun eine URL generieren, um den Bot  in Discord einem Server hinzuzufügen. 

# Im OAuth2 URL-Generator den Anwendungsbereich definieren
# bot anhacken

# Im Bereich Botberechtiegung auswählen, was benötigt wird.
# Rollen verwrwalten, Kaäle verwarlten, Kanäle ansehn, Nachrichten Senden, Nachrichten senden, Nachrichten verwalten, 
# Links einbetten, Datein anhängen, Nachrichtenverlauf anzeigen, Externe Stricker verwenden, Slash-Befehle verwenden, verbinden, prechen

 

## ---------    03 - Projekt erstellen --------##

# Den Konfigurierten Bot einem Discordserver hinzufügen:
# URL in den Browser patsen, anschliessend wird man in die Discord app weitergeleitet und fügt ihn dort einen Server hinzu.

# Als nächstes legen wir ein neues Python Projekt an.
#
# Schrit 1: Neuen Folder erzeugen
    # Achtung wenn virtuelle umgebung noch aktiv aus einem altem projekt, erst deaktivieren.
    # In den Pfad des voriegen Projekts wechseln dann das eingeben : deactivate

# schrit 2: auf dem Ordner Pfad wechseln
# schrit 3: Virtuelle umgebung erzeugen : python -m venv .venv
# schrit 4: .env om Projektfolder erzeugen.
# schrit 5: Virtuelle umgebung aktivieren über cmd : ".venv/Scripts/activate"
# Schrit 6: Installieren 2 Pakages über Pip install, Discord.py und dotenv : pip install discord.py python-dotenv 

# schrit 7: main.py im Projektordner anlegen. 
# schrit 8: Imports in der main.py  vornehmen, 
    # import discrod
    # from dotenv import load_dotenv
    # import os

# schrit 9: Discord Token in der .env anlelegen
    # DISCORD_TOKEN = token

# schrit 10: DISCORD_KEY aus der .env in die main.py holen 
    #  load_dotenv()
    # token = os.get_env('DISCORD_TOKEN')
    # testweise printen = print(token)
    # über cmd testen : python main.py / ob der token ausgegebn wird.

# Wichtig, sollte was Grün unterkringelt sein von den Imports, prüfen man auf dem richtigen Python interpreter sich befindet:
    # vd code Strg + Shift + P
    # Python: Select Interpreter
    # Akltuellen projektpfad wählen Projekt\.venv\Scripts\python.exe




## ---------     04 - Bot starten --------##

# Doku https://discordpy.readthedocs.io/en/stable/ext/commands/index.html
# https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#bots

# Schrit 11: Es werden ein weiterer import benötigt
    # from discrod.ext import commands
    
# Schrit 12: 
    # intents = discord.Intents.default() 
    # bot = commands.Bot(command_prefix='!', intents=intents)

    # intents ist die Erlaubnis, was ein Bot darf und was nicht.
    # command_prefix='!' dient dazu den Bot über ein gewisses zeichen anzusprechen und befehle zu übergeben oder aktion zu triggern.

# Schrit 13: bot event hinzufügen
    # @bot.event                          # Discord.py bot event
    # async def on_ready():               # wenn der bot gestartet ist ... 
    # print(f'ready! Und ich bin {bot.user}')  # printet er das       

    # bot.run(token)                      # bot komplett gestartet. 



## ---------    05 - Logging mit Python --------##
 
    # Link zur Doku:
    #https://docs.python.org/3/library/logging.handlers.html#logging.FileHandler

# Wir implementieren einen FileHandler als logger um fehler zu tracken 

# Schrit 1: Handler importieren
    # import logging hinzufügen oben.

# schrit 2: handler anlegen 
    # handler = logging.FileHandler(filename="discordbot.log", mode='w', encoding="utf-8")
        # filename="discordbot.log" = Name der Datei die erzeugt wird vom logger
        # mode='w' steht für write also schreiben
        # encoding="utf-8" = Welche Zeichen und utf standard verwendet wird

# Schrit 3: handler aufrufen/satrten bei Programmstart
    #  wir fügen der Start fucktion "bot.run(token)" weitere Parameter hinzu. 
    # bot.run(token, log_handler=handler, log_level=logging.DEBUG)  



## ---------   06 - Nachrichten operationen --------##

    #Link zur Doku:
    #https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#bots

# Schrit 1: in die Developers/applications einstellungen vom bot gehn auf Discord
    #https://discord.com/developers/applications/1535232540741341306/bot
    # dort Server Members Intent & Message Content Intent aktivieren 
    
# Schrit 2: intents erweitern / was der bot darf un kann
    # intents.message_content = True      
    # ermöglicht es auf Massages zu reagieren

    # intents.members = True  
    # ermöglicht es dem Mebers etwas zu sagen

# Schrit 3: on_message Event hinzufügen
    # @bot.event                      # Event on_message
    # async def on_message(message):  # Message wird geschickt wir können reagieren

    # if message.author == bot.user:   # Bot prüft ob die message von ihm  
    #    return                        #  selbst kommt  

    # if 'banana' in message.content.lower(): # wenn 'banana' in der nachricht 
    #    await message.delete()             # ist dann lösche sie
    #    channel = message.channel
    #    await channel.send(f'Hey dieser Begriff ist nur für die Schüler der DA geeignet {message.author}!')


    # await bot.process_commands(message) # wartet bis die Message process ist
                                        # reagiert nicht erneut auf die massage.



## ------------------     07 - Discord Commands ------------------##

#Link zur Doku:
#https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html

# Commands legen wir an wie Events am ende ist es ein Event welches durch ! ein command triggert

# @bot.command()                      # Command der durch !hallo ausgelöst wird
# async def hallo(ctx):
#    await ctx.send(f"Grüße dich {ctx.author.mention}") 

# @bot.command()
# async def msg(ctx, arg):
#    await ctx.send(f"deine Nachricht war {arg}") 




## -----------   08 - Rollen hinzufügen und entfernen -------------##

# Discord Server aufruffen, Oben auf dem Servernamen, die Servernamen einstellungen ausklappen - dann auf Rollen klicken.
# Um die Rollen verwenden zu können benötiegen wir Discor Utils aus der Doku

# Neue Rolle erstellen :

# Schrit 1: klicke auf Rolle Erstellen
    # Name vergeben und dann Änderung speichern.

# Schrit 2: neuen Command anlegen
    #new_role = 'hammerTyp'          

    # @bot.command()         # Command für die neu angelegte Rolle in diescrord
    # async def assign(ctx):
    # role = discord.utils.get(ctx.guild.roles, name=new_role)
    # if role:
    #   await ctx.author.add_roles(role)
    #   await ctx.send("Deine Rolle wurde nicht gefunden") 
    #   return
    # await ctx.send("Deine Rolle wurde hinzugefügt") 



