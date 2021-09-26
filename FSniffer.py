import collections
import math

class FSniffer:

    def __init__(self, cipher_text, min_chunk_len, alpha, most_fr):
        self.cipher_text = cipher_text
        self.min_chunk_len = min_chunk_len
        self.alpha = alpha
        self.alpha_size = len(alpha)
        self.most_fr = most_fr
        self.matrix = {}
        self.__BuildTableOfIndexes()

    def __BuildTableOfIndexes(self):  

        # (OK) Armazena possíveis tamanhos de chave com médias de índices de coincidência
        for keySize in range(self.alpha_size):
            for k in range(keySize):

                # Cria substrings
                encryptedChunk = str(self.cipher_text[k::keySize])

                # Só considera cadeias de texto cujo tamanho é maior ou igual ao tamanho mínimo definido para o bloco
                if len(encryptedChunk) >= self.min_chunk_len:
                    coincidenceIndex = self.__CalculateIndexOfCoincidence(encryptedChunk)
                    # Considera apenas índices diferentes de 0
                    if coincidenceIndex > .0:
                        if keySize in self.matrix:
                            self.matrix[keySize].append(coincidenceIndex)
                        else:
                            self.matrix[keySize] = [coincidenceIndex]
            # Calcula a média de índices para cada tamanho de chaves
            if keySize in self.matrix:
                self.matrix[keySize] = float(sum(self.matrix[keySize]) / len(self.matrix[keySize]))

    # Calcula o índice de coincidência
    def __CalculateIndexOfCoincidence(self, encryptedChunk):
        calculate_frequency = collections.Counter(encryptedChunk)

        frequency_sum = 0.0
        # Calcula o somatório das frequências 
        for char_frequency in calculate_frequency.values():
            frequency_sum = frequency_sum + char_frequency * (char_frequency - 1)

        text_size = len(encryptedChunk)
        return frequency_sum / (text_size * (text_size - 1))

    # Realiza uma distribuição e guarda a soma das distribuições, para que assim seja possível descobrir quem é o melhor candidato
    def _GetFrequencyTestSum(self, frequencies, totalLength):
        totalSum = 0.0
        for f in frequencies:
            frequencies[f] *= (1.0 / totalLength)
            totalSum += ((frequencies[f] - math.pow(self.alpha[f], 2)) / self.alpha[f])
        return totalSum

    # Realiza o deslocamento dos caracteres para decifrar o texto 
    def _GetLetterDisplacements(self, encryptedChunk, position):
        displacements = []
        alphabetSize = self.alpha_size
        for letter in encryptedChunk:
            displacement = chr(ord(self.most_fr) + ((ord(letter) - ord(self.most_fr) - position) % alphabetSize))
            displacements.append(displacement)
        return displacements

    # De acordo com o cálculo da distribuição, escolhe a letra cujo a frequência mais se aproxima do índice da língua portuguesa
    def GetBestLetterGuess(self, encryptedChunk):
        sums = {}
        alphabetLength = self.alpha_size
        
        for i in range(alphabetLength):
            displacements = self._GetLetterDisplacements(encryptedChunk, i)
            frequencies = collections.Counter(displacements)
            sums[i] = self._GetFrequencyTestSum(frequencies, len(encryptedChunk))
            letterReplaced = min(sums, key = sums.get) + ord(self.most_fr)
            
        return chr(letterReplaced)
    
    def GetMatrix(self):
        return self.matrix

    def GetEncryptedText(self):
        return self.cipher_text

