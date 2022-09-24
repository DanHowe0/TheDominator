import discord
from discord.ext import commands
import time

class Roles(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  #@commands.has_permissions(Administrator=True)
  async def stress_roles(self, ctx):
    index=0

    while True:
      time.sleep(1)
      try:
        role = await ctx.guild.create_role(name=index, colour=discord.Color.from_rgb(index, index, index))
        await ctx.author.add_roles(role)
      except Exception as f:
        await ctx.send(f)
        return

      index += 1

def setup(client):
  client.add_cog(Roles(client))

