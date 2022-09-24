import discord
from discord.ext import commands, tasks

class Admin(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user : discord.Member, *, reason="Ban Hammer Has Spoken"):
    if user.id == ctx.author.id:
      await ctx.send("You cant ban yourself silly!")
      return
    await user.ban(reason=reason)
    await ctx.send(f"{user.name}#{user.discriminator} has been banned for {reason}")

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unban(self, ctx, user):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
            
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user: discord.Member, *reason):
    await user.kick(reason=reason)

  # https://discordpy.readthedocs.io/en/latest

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, amount=10, user: discord.Member = None):
    channel = ctx.channel
    await ctx.message.delete()
    if user == None:
      await channel.purge(limit=int(amount))
    else:
      await channel.purge(limit=int(amount), check=lambda message: message.author == user)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def announce(self, ctx, channel, *, message):
    await ctx.message.delete()
    
    if channel.startswith("<#"):
      channel = discord.utils.get(ctx.guild.text_channels, id=int(channel[2:-1]))
    else:
      channel = discord.utils.get(ctx.guild.text_channels, id=int(channel))

    await channel.send(message)
      

def setup(client):
  client.add_cog(Admin(client))