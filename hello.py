import random

def insult_me():
	insults = ["You are dumb", "You are stupid", "You are slow"]
	return random.choice(insults)

my_insult = insult_me()
print my_insult