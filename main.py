import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
import random


import json # store data in external files

def prefix(ctx, arg):
  with open("bot.json", "r") as file: # opens the json file in read "r" mode
    data = json.load(file) # load the file into the variable "data"
    return data["prefix"] # gets the prefix from the data and returns it as the prefix

client = commands.Bot(
	command_prefix=prefix,  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

client.author_id = ["451450518141665292", "428369959501168650", "310806196330168320"]  # Change to your discord id!!!

client.links = {
  "twitch": "https://twitch.tv/HALO_oliver" # can put all links in here and the client will store them for use
}

@client.event
async def on_message(msg):
  #Dont respond if the author is the bot
  if msg.author.bot:
    return

  # VROOOOOM
  if msg.channel.id == 1016750874372091985:
    vrooms = []
    for word in msg.content.split(" "):
     if "vroom" in word.lower():
      vroom = ["V", "R"]
      for i in range(0, random.randint(2, 12)):
        vroom.append("O")
      vroom.append("M")
      vrooms.append("".join(vroom))
    if len(vrooms) > 0:
      await msg.channel.send(" ".join(vrooms))

  # DM handler
  #if msg.channel.type == discord.ChannelType.private:
    #channel = client.get_channel(952983131252744202) 
    # 815995867555299369 <-- test server 

    #embed = discord.Embed(title="New DM")
    #embed.add_field(name="User Info", value=f"User: {msg.author}\nUser ID: {msg.author.id}", inline=False)
    #embed.add_field(name="Message", value="None" if msg.content == "" else msg.content, inline=False)
    #print(msg)

    #index=1
    #for i in msg.attachments:
      #embed.add_field(name="Image "+str(index), value=i.url)
      #index+=1

    #await channel.send(embed=embed)
    
  await client.process_commands(msg)

for cog in os.listdir("./cogs"): # loops through all the files in the cogs folder
  if cog.endswith(".py"): # if its a python file then continue
    client.load_extension(f"cogs.{cog[:-3]}") # load the cog into the client


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_CLIENT_SECRET") 
client.run(token)  # Starts the client