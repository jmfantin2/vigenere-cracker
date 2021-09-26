import string

class KMaker:
    def __init__(self, frequency, alpha, lang_coindex):
        self.frequency = frequency
        self.alpha_size = len(alpha)
        self.lang_coindex = lang_coindex
        self.matrix = frequency.GetMatrix()

    def GetKeyLength(self):
        getClosestFrequency = lambda k : abs(float('%.3f' % k[1]) - self.lang_coindex)
        key,_ = min(self.matrix.items(), key = getClosestFrequency)
        return key

    def GetPassword(self):
        keyLength = self.GetKeyLength()
        encryptedText = self.frequency.GetEncryptedText()
        return ''.join(self.frequency.GetBestLetterGuess(encryptedText[k::keyLength]) for k in range(keyLength))

    def GetPlainText(self):
        password = self.GetPassword()
        encryptedText = self.frequency.GetEncryptedText()
        return ''.join(string.ascii_lowercase[(ord(char) - ord(password[pos % len(password)])) % self.alpha_size] for pos, char in enumerate(encryptedText))
