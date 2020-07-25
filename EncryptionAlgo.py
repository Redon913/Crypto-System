
import string

alphabetUpper = string.ascii_uppercase      #calling all uppercase ascii in a string list
alphabetLower = string.ascii_lowercase      #calling all lowercase ascii in a string list
digits = string.digits          #taking Digits as string list


'''-------------------------------------------Caesar Cipher-----------------------------------------------'''
class CaesarCipher:

    def __init__(self, plainText, key):
        self.plainText = plainText
        self.__key = key

    def __logic(self):
        self.__cipher = ""
        __codes = []

        for Alpha in self.plainText:
            if Alpha in alphabetLower:
                textIndex = (alphabetLower.index(Alpha) + self.__key) % 26
                __codes.append(alphabetLower[textIndex])

            elif Alpha in alphabetUpper:
                textIndex = (alphabetUpper.index(Alpha) + self.__key) % 26
                __codes.append(alphabetUpper[textIndex])
            
            else:
                __codes.append(Alpha)

        self.__cipher = self.__cipher.join(__codes)        
        
    def CipherText(self):
        self.__logic()
        return self.__cipher

'''-------------------------------------------Vigenere Cipher-----------------------------------------------'''
class VigenereCipher:

    def __init__(self, plainText, key):
        self.plainText = plainText
        self.__key = key
        self.__keyCount = 0
        self.__keyLen = len(self.__key)

    def __logic(self):
        self.__cipher = ""
        __ciphers = []

        for Alpha in self.plainText:
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
                textIndex = (alphabetLower.index(Alpha) + keyindex) % 26
                __ciphers.append(alphabetLower[textIndex])

            elif Alpha in alphabetUpper:
                textIndex = (alphabetUpper.index(Alpha) + keyindex) % 26
                __ciphers.append(alphabetUpper[textIndex])

        #     IF NEED TO SHIFT DIGITS TOO

            elif Alpha in digits:
                textIndex = (digits.index(Alpha) + keyindex) % 10
                __ciphers.append(digits[textIndex])

            else:
                __ciphers.append(Alpha)

        self.__cipher = self.__cipher.join(__ciphers)

    def CipherText(self):
        self.__logic()
        return self.__cipher

'''-------------------------------------------Rail Fence Cipher-----------------------------------------------'''

class RailFence:

    def __init__(self, plainText, key):
        self.__plainText = plainText
        self.__key = key

    def __logic(self):
        self.__cipherText = ""
        self.__ciphers  = [[] for j in range(self.__key)]
        self.__keyCount = 0
        sign = 1

        for Alpha in self.__plainText:
            self.__ciphers[self.__keyCount].append(Alpha)

            self.__keyCount += sign
            if self.__keyCount == self.__key - 1:
                sign *= -1
            if self.__keyCount == 0:
                sign *= -1
        
        for l in self.__ciphers:
            temp = ''
            temp = temp.join(l)
            self.__cipherText += temp

    def CipherText(self):
        self.__logic()
        return self.__cipherText