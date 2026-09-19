import discord                      # Importiert Discord Pagaes
from dotenv import load_dotenv      # stellt die Function load_dotenv from 
                                    # dotenv bereit
import os                           # Import Operatet System
from discord.ext import commands    # stellt die command von discord.ext bereit
import logging

handler = logging.FileHandler(filename="discordbot.log", mode='w', encoding="utf-8")

load_dotenv()                       # läd die .env in main.py
token = os.getenv('DISCORD_TOKEN')  # legt den DISCORD_TOKEN in token ab.

intents = discord.Intents.default() # Regeln die für den Bot gelten festgelgt

intents.message_content = True      # ermöglicht das reagieren auf nachrichten
intents.members = True              # ermöglicht es dem Mebers etwas zu sagen

bot = commands.Bot(command_prefix='!', intents=intents) # Bot erstellt

@bot.event                          # Discord.py bot event
async def on_ready():               # wenn der bot gestartet ist ... 
    print(f'ready! Und ich bin {bot.user}')  # printet er das  



@bot.command()                      # Command der durch !hallo ausgelöst wird
async def hallo(ctx):
    await ctx.send(f"Grüße dich {ctx.author.mention}") 

@bot.command()
async def msg(ctx, arg):
    await ctx.send(f"deine Nachricht war {arg}") 

# ----- rollen hinzufügen und entfernen------ #
new_role = 'hammerTyp'           # Rollen bezeichnung in Discord auf dem Server

@bot.command()               # Command für die neu angelegte Rolle in diescrord
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send("Deine Rolle wurde nicht gefunden") 
        return
    await ctx.send("Deine Rolle wurde hinzugefügt") 

@bot.command()               # Command für die neu angelegte Rolle in diescrord
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send("Deine Rolle wurde entfernt") 
        return
    await ctx.send("Deine Rolle wurde nicht gefunden") 



@bot.event                      # Event on_message
async def on_message(message):  # Message wird geschickt wir können reagieren

    if message.author == bot.user:   # Bot prüft ob die message von ihm kommt   
        return

    if 'banana' in message.content.lower(): # wenn 'banana' in der nachricht ist
         await message.delete()             # dann lösche sie
         channel = message.channel
         await channel.send(f'Hey dieser Begriff ist nur für die Schüler der DA geeignet {message.author}!')


    await bot.process_commands(message) # wartet bis die Message process ist
                                        # reagiert nicht erneut auf die massage.


bot.run(token, log_handler=handler, log_level=logging.DEBUG)                      # bot komplett gestartet. 