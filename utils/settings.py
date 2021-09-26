'''
  Utilize este arquivo para escolher uma das cifras
  e alterar variáveis importantes para a execução.
'''

import os

# 1 ARQUIVO DA CIFRA
PROJ_PATH = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILE_PATH = PROJ_PATH + '\\files\\cipher4.txt'

def read():  
  with open(FILE_PATH, 'r') as file:
      # copy text from file 
      return file.read()

# 2 ————————————————————————————————————————————————————————————

scheduler_settings = {
  'seed': 3,
  'a': 33,
  'c': 11,
  'm': 2 ** 31, #2^31
  'first_in': 3,
  'last_gen': 100000
}

def getSS():
  return scheduler_settings

# ——————————————————————————————————————————————————————————————

def log():
  print('These are your settings:\n')
  print('LCD seed:', scheduler_settings.get('seed'))
  print('LCD a   :', scheduler_settings.get('a'))
  print('LCD c   :', scheduler_settings.get('c'))
  print('LCD m   :', scheduler_settings.get('m'))
  print('1st arr.:', scheduler_settings.get('first_in'))
  print('Stops at:', scheduler_settings.get('last_gen'))

  for q in queue_settings:
    print()
    print('( Q'+str(q), ') a dist.:', str(queue_settings[q].get('a_min'))+'..'+str(queue_settings[q].get('a_max')))
    print('( Q'+str(q), ') b dist.:', str(queue_settings[q].get('b_min'))+'..'+str(queue_settings[q].get('b_max')))
    print('( Q'+str(q), ') cervers:', queue_settings[q].get('c'))
    print('( Q'+str(q), ') kpacity:', queue_settings[q].get('k'))
