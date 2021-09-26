'''
  Utilize este arquivo para escolher uma das cifras
  e alterar __variáveis importantes para a execução.
'''

# 1 ARQUIVO DA CIFRA ———————————————————————————————————————————

import os

__cipher = 'cipher4.txt'

PROJ_PATH = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILE_PATH = PROJ_PATH + '\\files\\' + __cipher

def read():  
  with open(FILE_PATH, 'r') as file:
      return file.read()

# 2 ————————————————————————————————————————————————————————————

''' 
Observação:
  lang_coindex (PT) = 1.93/26 = 0.0742
  lang_coindex (EN) = 1.76/26 = 0.0677
Retirado de https://en.wikipedia.org/wiki/Letter_frequency
''' 

__vars = {
  'min_chunk_len': 2,
  'lang': 'pt', #pt || en
  'lang_coindex': 0.072723, # pt 0.0742 || en 0.0677
  'alpha': {'lang': 'PT','a':0.1463,'b':0.0104,'c':0.0388,'d':0.0499,'e':0.1257,'f':0.0102,'g':0.013,'h':0.0078,'i':0.0618,'j':0.039,'k':0.001,'l':0.0277,'m':0.0473,'n':0.0444,'o':0.0973,'p':0.0252,'q':0.012,'r':0.0653,'s':0.068,'t':0.0433,'u':0.0363,'v':0.0157,'w':0.0003,'x':0.0025,'y':0.0006,'z':0.0047}
  #'alpha': {'lang': 'EN','a':0.0816,'b':0.0149,'c':0.0278,'d':0.0425,'e':0.127,'f':0.0222,'g':0.02,'h':0.0609,'i':0.0696,'j':0.0015,'k':0.0077,'l':0.0402,'m':0.024,'n':0.0675,'o':0.075,'p':0.0192,'q':0.0009,'r':0.0598,'s':0.0632,'t':0.0905,'u':0.0275,'v':0.0098,'w':0.0236,'x':0.0015,'y':0.0197,'z':0.0007}
}

# ——————————————————————————————————————————————————————————————

