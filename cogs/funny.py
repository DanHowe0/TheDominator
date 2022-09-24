import os
import discord
from discord.ext import commands

from typing import Optional

def ext_save(s):
  global funny
  funny = s

class Funny(commands.Cog):
  def __init__(self, client):
    self.client = client
    self._lock = True
    ext_save(self)

  def lock():
    def predicate(ctx):
        global funny
        return funny._lock
    return commands.check(predicate)

  @commands.command(hidden=True)
  @commands.has_any_role(945383174006014042, 806492184718737408)
  async def funnylock(self, ctx, state="off"):
    if state.lower() == "off":
      self._lock = True
    elif state.lower() == "on":
      self._lock = False

    ext_save(self)
    

  @commands.command()
  @lock()
  async def spank(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.spank = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been spanked by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def attack(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.attack = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been attacked by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def hug(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.hug = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been hugged by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def stomp(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.stomp = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been stomped on by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def pat(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.pat = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been head-patted by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def high5(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.high5 = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been high fived by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def fuck(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.fuck = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been fucked by {ctx.author.mention}, hope they had consent")

  @commands.command()
  @lock()
  async def twirl(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.twirl = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{ctx.author.mention} Has twirled for {tag.mention}")

  @commands.command()
  @lock()
  async def wink(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.wink = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{ctx.author.mention} Has winked at {tag.mention}")

  @commands.command()
  @lock()
  async def spoon(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.spoon = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been spooned by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def slap(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.slap = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been slapped by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def kiss(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.kiss = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been kissed by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def smack(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.smack = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been smacked by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def hit(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.hit = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been hit by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def throw(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.throw = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been thrown by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def cuddle(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.cuddle = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been cuddled by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def snuggle(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.snuggle = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been snuggled by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def glomp(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.glomp = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been glomped by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def bite(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.bite = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been bitten by {ctx.author.mention}")

  @commands.command()
  @lock()
  async def catcall(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.catcall = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been catcalled by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def poke(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.poke = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been poked by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def tickle(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.tickle = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been tickled by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def tease(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.tease = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been teased by {ctx.author.mention} very naughty")
  
  @commands.command()
  @lock()
  async def punt(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.punt = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been puntted by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def nibble(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.nibble = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been nibbled by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def shank(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.shank = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been shanked by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def fight(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.fight = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been fought by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def ignore(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.ignore = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been ignored by {ctx.author.mention} how very rude of them!")
  
  @commands.command()
  @lock()
  async def trip(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.trip = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been tripped by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def serenade(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.serenade = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been serenaded by {ctx.author.mention}")
  
  @commands.command()
  @lock()
  async def punch(self, ctx, tag: Optional[discord.Member]=None, *args):
    self.punch = False
    await ctx.send("Tag another person you dummy" if (tag == None or tag == ctx.author) else f"{tag.mention} Has been punch by {ctx.author.mention}")
  
  @commands.command(hidden=True)
  @lock()
  async def UwU(self, ctx):
    await ctx.message.delete()
    #for i in range(0, 10):
    await ctx.send("UwU")

def setup(client):
  client.add_cog(Funny(client))

#something here breaks the bot so i made it a text file
#was this before?
