from random import randrange
# not the actual random number generator requested. that's just for fun.

quotes = ('I\'ve never found it hard to hack most people.\nIf you listen to them, watch them, their vulnerabilities are like a neon sign screwed into their heads.\n — Mr Robot (2013)',
'Alright.\nTear it down, light it up, sweep away the ashes.\n — The Imitation Game (2014)')

def greet():
  print(quotes[0])

def loading(n):
  if n == 0:
    print('capturando cifra..')
  elif n == 1:
    print('analisando frequências..')
  elif n == 2:
    print('forjando chave..')
  else:
    print('furtando informações..')

def goodbye():
  print(quotes[1])

def mkLine():
  print('\n——————————————————————————————\n')
