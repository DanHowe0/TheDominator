import discord
from discord.ext import commands

class Error(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
      """A global error handler cog."""

      if isinstance(error, commands.CommandNotFound):
          return  # Return because we don't want to show an error for every command not found

      if isinstance(error, commands.CheckFailure):
          return
        
      elif isinstance(error, commands.CommandOnCooldown):
          message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        
      elif isinstance(error, commands.MissingPermissions):
          message = "You are missing the required permissions to run this command!"
        
      elif isinstance(error, commands.UserInputError):
          message = "Something about your input was wrong, please check your input and try again!"

      elif isinstance(error, commands.PrivateMessageOnly):
          message = "This command can only be used in DMs, message <@816699672722145371> to use this"
        
      else:
          message = "Oh no! Something went wrong while running the command!"
          print(error)

      await ctx.send(message)

def setup(client):
  client.add_cog(Error(client))