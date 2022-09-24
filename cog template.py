# define all your imports at the top of your code
# discord and discord.ext.commands are essential to make the code run

import discord
from discord.ext import commands

# you can add other imports here as and when you need them




# next, define the name of the section of commands:
class Name(commands.Cog): # commands.Cog will tell the bot that this is a Cog

  def __init__(self, client): # __init__ is called when the "class" is initialised, useful to store initial data when its activated
    self.client = client




  # next up you will need a "check" function, so only people who pass the check can activate the command.
  # There are built in checks already like @commands.has_permissions

  def check_name(self, ctx): # rename this to be relevant with what you are checking for
    if ctx.author.id in self.client.author_id:
      return True # checks should always return True or False

      # True = the user can do the command
      # False = the user cannot do the command





  # next we have to tell the client that the next function is going to be a command
  @commands.command()
  #we can pass arguments to the @commands.command() like so:

  # @commands.command(
  #   aliases = [""],
  #   description = ""
  # )

  # full list of args you can pass with explainations of what they do: 
  # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.command
  # on the left hand side

  # now we tell the bot to perform the check
  @commands.check(check_name) # change "check_name to the name of the relevant check"

  # to check if a user has permissions you can do:
  # @commands.has_permissions(permission_name=True)
  # all permission names are here https://discordpy.readthedocs.io/en/latest/api.html?#discord.Permissions

  # to check if a user has a specific role in the guild you can do:
  # @commands.has_role(role_name_or_id)
  # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?#discord.ext.commands.has_role


  # next we define the function where the code we need to run will go
  def command_name(self, ctx, arg1, arg2, *args):
    #command_name will be the name used to activate the command unless you have specified a name in @commands.command

    # arg1 and arg2 take the next 2 words in the command from discord stores them
    # *args takes any extra words and stores them in a list so the bot doesnt break when too many words are entered.

    # you can also put (self, ctx, arg1=value, arg2=value, *args) so that if there was nothing entered the bot wont crash


    # now you can put whatever code you need here to make the bot do whatever you want
    
    pass # this tells the command to do nothing as this is just a template



# Finally, we need to tell the bot to add the cog to the itself

def setup(client): # this is called when we tell the bot to "load_extension"
  client.add_cog(Name(client)) # here we add the cog to the client