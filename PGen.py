  
import random
import pyperclip

class PGen :

    def __init__(self):
        pass
        

    def GeneratePassword(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        upper = letters.upper()
        numbers = "0123456789"
        symbols = "&é()*;:,/+=~%£µ^$"
        all = letters + upper + numbers + symbols
        length = 16
        password = "".join(random.sample(all,length))

        return password

