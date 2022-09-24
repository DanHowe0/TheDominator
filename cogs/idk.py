# define all your imports at the top of your code
# discord and discord.ext.commands are essential to make the code run

import discord
from discord.ext import commands

# you can add other imports here as and when you need them




# next, define the name of the section of commands:
class Name(commands.Cog): # commands.Cog will tell the bot that this is a Cog

  def __init__(self, client): # __init__ is called when the "class" is initialised, useful to store initial data when its activated
    self.client = client

  # next we have to tell the client that the next function is going to be a command
  @commands.command()
  async def im(self, ctx, word, *args):
    await ctx.send(f"Hi {word}, Im <@816699672722145371>")

def setup(client):
  client.add_cog(Name(client)) # here we add the cog to the client