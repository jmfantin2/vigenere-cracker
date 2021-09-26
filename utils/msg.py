from random import randrange
# not the actual random number generator requested. that's just for fun.

greetings = ('Welcome, my son.\nWelcome to the machine.\n — Pink Floyd (1975)',
'Remember, all I’m offering is the truth.\nNothing more.\n — Matrix (1999)',
'I\'m going on an adventure!\n — The Hobbit (1937)',
'Hello.\nI\'ve waited here for you... everlong.\n — Foo Fighters (1997)',
'What the hell are you doing here?\n — 1917 (2020)',
'Memory is a strange thing.\n — Arrival (2016)',
'Alright.\nTear it down, light it up, sweep away the ashes.\n — The Imitation Game (2014)')

def greet():
  rand = randrange(7)
  print(greetings[rand])

def mkLine():
  print('\n——————————————————————————————\n')
