import string

class KMaker:
    def __init__(self, frequency, alpha, lang_ic):
        self.frequency = frequency
        self.alpha_size = len(alpha)
        self.lang_ic = lang_ic
        self.ic_table = frequency.getIcTable()

    def getKeySize(self):
        getNearFrequency = lambda k : abs(float('%.3f' % k[1]) - self.lang_ic)
        key,_ = min(self.ic_table.items(), key = getNearFrequency)
        return key

    def getKey(self):
        key_size = self.getKeySize()
        cipher = self.frequency.getCipher()
        return ''.join(self.frequency.getProbableLetter(cipher[k::key_size]) for k in range(key_size))

    def revealOriginalText(self):
        key = self.getKey()
        cipher = self.frequency.getCipher()
        return ''.join(string.ascii_lowercase[(ord(char) - ord(key[pos % len(key)])) % self.alpha_size] for pos, char in enumerate(cipher))
