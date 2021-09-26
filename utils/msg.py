from random import randrange
# not the actual random number generator requested. that's just for fun.

greetings = ('I\'ve never found it hard to hack most people.\nIf you listen to them, watch them, their vulnerabilities are like a neon sign screwed into their heads.\n — Mr Robot (2013)',
'Alright.\nTear it down, light it up, sweep away the ashes.\n — The Imitation Game (2014)')

def greet():
  rand = randrange(2)
  print(greetings[rand])

def mkLine():
  print('\n——————————————————————————————\n')

def loading():
  print('loading...')
