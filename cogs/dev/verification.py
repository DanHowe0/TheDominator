import discord
from discord.ext import commands

class Verification(commands.Cog):
  def __init__(self, client):
    self.client = client

  def do_check(ctx):
    return False # disable until we know what were doing with it

  @commands.command()
  @commands.dm_only()
  @commands.check(do_check)
  async def verify(self, ctx, *args):
    dm_ids = [943959540028817459, 451450518141665292, 779442734091206676]
    dm_ids = [428369959501168650, 451450518141665292]

    embed = discord.Embed(title="New DM")
    embed.add_field(name="User Info", value=f"User: {ctx.author}\nUser ID: {ctx.author.id}", inline=False)
    embed.add_field(name="Message", value="None" if ctx.message.content == "=verify" else ctx.message.content[7:], inline=False)

    index=1
    for i in ctx.message.attachments:
      print(i.url)
      embed.add_field(name="Image "+str(index), value=i.url)
      index+=1

    for i in dm_ids:
      member = await self.client.fetch_user(i)
      channel = await member.create_dm()
      await channel.send(embed=embed)

def setup(client):
  client.add_cog(Verification(client))