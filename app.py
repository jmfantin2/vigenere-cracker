from utils import msg, settings

"""
INICIA AS VARIÁVEIS
"""

# texto cifrado
cipher = ''
# tamanho da chave
key_size = 0
# indice de coincidencia
coindex = 0

cipher = settings.read()

"""
DESCOBRE O TAMANHO DA CHAVE (2 A 20)
"""

### QUEBRA A STRING A CADA KEY SIZE (2 A 20)
# credit: https://stackoverflow.com/questions/9475241/split-string-every-nth-character
def textChunks(text, key_size):
  chunks = [text[i:i+key_size] for i in range(0, len(text), key_size)]
  return chunks
  
  ### TODO CALCULA O INDICE DE COINCIDENCIA
  # LOCK-ON NUM IC PRA TODAS AS SUBSTRINGS = ACHOU O TAMANHO
  
  # ATUALIZA COINDEX E KEY_SIZE

###################

textChunks(cipher, 2)
