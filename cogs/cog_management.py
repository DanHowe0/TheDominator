import discord
from discord.ext import commands

class DevCommands(commands.Cog, name='Developer Commands'):
  '''These are the developer commands'''

  def __init__(self, client):
    self.client = client



  @commands.command(  # Decorator to declare where a command is.
		name='reload',  # Name of the command, defaults to function name.
		aliases=['rl']  # Aliases for the command.
  ) 
  async def reload(self, ctx, cog=None):
    '''
    Reloads a cog.
    '''
    extensions = self.client.extensions
    if cog == 'all' or cog == None:  # Lets you reload all cogs at once
      for extension in extensions:
        self.client.unload_extension(extension)
        self.client.load_extension(extension)
        await ctx.send(f'Done `{extension.split(".")[1]}`')
    elif cog in extensions:
      self.client.unload_extension(cog)  # Unloads the cog
      self.client.load_extension(cog)  # Loads the cog
      await ctx.send('Done')  # Sends a message where content='Done'
    else:
      await ctx.send('Unknown Cog')  # If the cog isn't found/loaded.
	
  @commands.command(name="unload", aliases=['ul']) 
  async def unload(self, ctx, cog=None):
    '''
    Unload a cog.
    '''
    extensions = self.client.extensions
    if cog not in extensions:
      await ctx.send("Cog is not loaded!")
      return
    self.client.unload_extension(cog)
    await ctx.send(f"`{cog}` has successfully been unloaded.")

  @commands.command(name="load")
  async def load(self, ctx, cog):
    '''
    Loads a cog.
    '''
    try:

      self.client.load_extension(cog)
      await ctx.send(f"`{cog}` has successfully been loaded.")

    except commands.errors.ExtensionNotFound:
      await ctx.send(f"`{cog}` does not exist!")

  @commands.command(name="listcogs", aliases=['lc'])
  async def listcogs(self, ctx):
    '''
    Returns a list of all enabled commands.
    '''
    base_string = "```css\n"  # Gives some styling to the list (on pc side)
    base_string += "\n".join([str(cog) for cog in self.client.extensions])
    base_string += "\n```"
    await ctx.send(base_string)


def setup(client):
  client.add_cog(DevCommands(client))