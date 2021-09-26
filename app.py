import os
from FSniffer import FSniffer
from KMaker import KMaker

from utils import msg

# PARA ESCREVER O TEXTO ORIGINAL NA PASTA outputs, DESCOMENTE A LINHA 50

''' 
Observações:
  LANG_IC (PT) = 1.94/26 = 0.0746
  > Retirado de https://en.wikipedia.org/wiki/Index_of_coincidence
  ALPHA { ... } 
  > Retirado com esforço de https://en.wikipedia.org/wiki/Letter_frequency
''' 

MIN_CHUNK_LEN = 2
ALPHA = {'a':0.1463,'b':0.0104,'c':0.0388,'d':0.0499,'e':0.1257,'f':0.0102,'g':0.013,'h':0.0078,'i':0.0618,'j':0.0039,'k':0.0001,'l':0.0277,'m':0.0473,'n':0.0444,'o':0.0973,'p':0.0252,'q':0.012,'r':0.0653,'s':0.068,'t':0.0433,'u':0.0363,'v':0.0157,'w':0.0003,'x':0.0025,'y':0.00006,'z':0.0047}
MOST_FR = 'a'
LANG_IC = 0.0746

INPUT = 'cipher16.txt'
PROJ_PATH = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
INPUT_PATH = PROJ_PATH + '\\utils\\inputs\\' + INPUT
OUTPUT = 'cracked16.txt'
OUTPUT_PATH = PROJ_PATH + '\\utils\\outputs\\' + OUTPUT

def readInput():  
  with open(INPUT_PATH, 'r') as file:
    return file.read()

def writeOutput(decipher_text):  
  with open(OUTPUT_PATH, "w+") as file:
    file.write(decipher_text)

if __name__ == "__main__":

  msg.mkLine()
  msg.greet()
  msg.mkLine()

  msg.loading(0)
  cipher_text = readInput()
  msg.loading(1)
  f_results = FSniffer(cipher_text, MIN_CHUNK_LEN, ALPHA, MOST_FR)
  msg.loading(2)
  keymaker = KMaker(f_results, ALPHA, LANG_IC)
  your_key = keymaker.getKey()
  msg.loading(3)
  #writeOutput(keymaker.revealOriginalText())

  print('\nCrakeamos sua chave (', your_key, ')\n2400R$ no PIX ( b4a375a3-be31-4d06-a628-27300d62335e ) ou REVELAREMOS seus segredos')
  msg.mkLine()

  msg.goodbye()
  msg.mkLine()
