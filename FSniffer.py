import collections
import math

class FSniffer:

    def __init__(self, cipher_text, min_chunk_len, alpha, most_fr):
        self.cipher_text = cipher_text
        self.min_chunk_len = min_chunk_len
        self.alpha = alpha
        self.alpha_size = len(alpha)
        self.most_fr = most_fr
        self.ic_table = {}
        self.buildIcTable()

    def buildIcTable(self):  

        # stores possible key sizes w/ average ics
        for key_size in range(self.alpha_size):
            for k in range(key_size):
                
                cipher_chunk = str(self.cipher_text[k::key_size])

                if len(cipher_chunk) >= self.min_chunk_len:
                    ic = self.calcIc(cipher_chunk)
                    # only for non-zero ics
                    if ic > 0.0:
                        if key_size in self.ic_table:
                            self.ic_table[key_size].append(ic)
                        else:
                            self.ic_table[key_size] = [ic]
            # average ics for each size
            if key_size in self.ic_table:
                self.ic_table[key_size] = float(sum(self.ic_table[key_size]) / len(self.ic_table[key_size]))

    def calcIc(self, cipher_chunk):
        calculate_frequency = collections.Counter(cipher_chunk)

        frequency_sum = 0.0
        for char_frequency in calculate_frequency.values():
            frequency_sum = frequency_sum + char_frequency * (char_frequency - 1)

        text_size = len(cipher_chunk)
        return frequency_sum / (text_size * (text_size - 1))

    # runs distribution and keeps dists sum 
    # useful for finding the best candidate
    def getFrequencySum(self, frequencies, total_length):
        sum = 0.0
        for f in frequencies:
            frequencies[f] *= (1.0 / total_length)
            sum += ((frequencies[f] - math.pow(self.alpha[f], 2)) / self.alpha[f])
        return sum

    # fluctuates characters to unveil text 
    def getLetterFluctuations(self, cipher_chunk, position):
        fluctuations = []
        for letter in cipher_chunk:
            fluc = chr(ord(self.most_fr) + ((ord(letter) - ord(self.most_fr) - position) % self.alpha_size))
            fluctuations.append(fluc)
        return fluctuations

    # dist follow-up: picks nearest letter to lang ic by frequency
    def getProbableLetter(self, cipher_chunk):
        sums = {}
        
        for i in range(self.alpha_size):
            fluctuations = self.getLetterFluctuations(cipher_chunk, i)
            frequencies = collections.Counter(fluctuations)
            sums[i] = self.getFrequencySum(frequencies, len(cipher_chunk))
            letter_shifted = min(sums, key = sums.get) + ord(self.most_fr)
            
        return chr(letter_shifted)
    
    def getIcTable(self):
        return self.ic_table

    def getCipher(self):
        return self.cipher_text

