from flask import Flask
from threading import Thread
import random


app = Flask('')

@app.route('/')
def home():
  return "The bot is online"
	#return '<a href="https://discord.gg/xkJZqdbX6f">Join the Discord Server</a>'

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()

  # If you work on this, you can create a webpage for your bot. e.g. Rhythm