import os
from discord.ext import commands
from discord import Streaming, Game


class Info(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("I'm in")
    print(self.client.user) # Prints the client's username and identifier

    what_to_say = "with Rebekah sexually 😫"

    activity = Streaming(name=what_to_say, url="https://discord.gg/sXk6TAhmHd")#, url=self.client.links["twitch"])
    #activity = Game(name=what_to_say)

    await self.client.change_presence(activity=activity) # set the clients status

  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'My ping is {round(self.client.latency*1000)}ms!')



def setup(client):
  client.add_cog(Info(client))
