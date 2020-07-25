
import string

alphabetUpper = string.ascii_uppercase      #calling all uppercase ascii in a string list
alphabetLower = string.ascii_lowercase      #calling all lowercase ascii in a string list
digits = string.digits          #taking Digits as string list


'''-------------------------------------------Caesar Cipher-----------------------------------------------'''
class CaesarCipher:

    def __init__(self, cipherText, key):
        self.cipherText = cipherText
        self.__key = key

    def __logic(self):
        self.__plaintext = ""
        __texts = []

        for Alpha in self.cipherText:
            if Alpha in alphabetLower:
                textIndex = (alphabetLower.index(Alpha) - self.__key) % 26
                __texts.append(alphabetLower[textIndex])

            elif Alpha in alphabetUpper:
                textIndex = (alphabetUpper.index(Alpha) - self.__key) % 26
                __texts.append(alphabetUpper[textIndex])
            
            else:
                __texts.append(Alpha)

        self.__plaintext = self.__plaintext.join(__texts)        
        
    def PlainText(self):
        self.__logic()
        return self.__plaintext

'''-------------------------------------------Vigenere Cipher-----------------------------------------------'''
class VigenereCipher:

    def __init__(self, cipherText, key):
        self.cipherText = cipherText
        self.__key = key
        self.__keyCount = 0
        self.__keyLen = len(self.__key)

    def __logic(self):
        self.__plaintext = ""
        __plaintexts = []

        for Alpha in self.cipherText:
            if(self.__key[self.__keyCount] in alphabetLower):
                keyindex = alphabetLower.index(self.__key[self.__keyCount])
            elif(self.__key[self.__keyCount] in alphabetUpper):
                keyindex = alphabetUpper.index(self.__key[self.__keyCount])
            elif(self.__key[self.__keyCount] in digits):
                keyindex = digits.index(self.__key[self.__keyCount])
            self.__keyCount += 1

            if self.__keyCount == self.__keyLen:
                self.__keyCount = 0

            if Alpha in alphabetLower:
                textIndex = (alphabetLower.index(Alpha) - keyindex) % 26
                __plaintexts.append(alphabetLower[textIndex])

            elif Alpha in alphabetUpper:
                textIndex = (alphabetUpper.index(Alpha) - keyindex) % 26
                __plaintexts.append(alphabetUpper[textIndex])

        #     IF NEED TO SHIFT DIGITS TOO

            elif Alpha in digits:
                textIndex = (digits.index(Alpha) - keyindex) % 10
                __plaintexts.append(digits[textIndex])

            else:
                __plaintexts.append(Alpha)

        self.__plaintext = self.__plaintext.join(__plaintexts)

    def PlainText(self):
        self.__logic()
        return self.__plaintext

'''-------------------------------------------Rail Fence Cipher-----------------------------------------------'''

class RailFence:

    def __init__(self, cipherText, key):
        self.__cipherText = cipherText
        self.__key = key

    def __logic(self):
        self.__plaintext = ""
        self.__plainTexts  = [[] for j in range(self.__key)]
        self.__keyCount = 0
        self.__up = False
        sign = 1

        for Alpha in self.__cipherText:
            self.__plainTexts[self.__keyCount].append(Alpha)

            self.__keyCount += sign
            if self.__keyCount == self.__key - 1:
                sign *= -1
            if self.__keyCount == 0:
                sign *= -1

        prevLen = 0
        for l in range(len(self.__plainTexts)):
            self.__plainTexts[l] = list(self.__cipherText[prevLen: prevLen + len(self.__plainTexts[l])])
            prevLen += len(self.__plainTexts[l])
        
        self.__keyCount = 0
        self.__up = False
        sign = 1
        for Alpha in self.__cipherText:
            self.__plaintext += self.__plainTexts[self.__keyCount].pop(0)

            self.__keyCount += sign
            if self.__keyCount == self.__key - 1:
                sign *= -1
            if self.__keyCount == 0:
                sign *= -1
    
    def PlainText(self):
        self.__logic()
        return self.__plaintext
