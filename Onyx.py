from colorama import Fore, Back, Style
from cryptography.fernet import Fernet
import json
import os
import PGen
import base64
import random
import Opal
P = PGen.PGen()
Op = Opal.Opal()
print(Fore.RED+"""
                                                                               
                                                                               
     OOOOOOOOO                                                                 
   OO:::::::::OO                                                               
 OO:::::::::::::OO                                                             
O:::::::OOO:::::::O                                                            
O::::::O   O::::::Onnnn  nnnnnnnn yyyyyyy           yyyyyyyxxxxxxx      xxxxxxx
O:::::O     O:::::On:::nn::::::::nny:::::y         y:::::y  x:::::x    x:::::x 
O:::::O     O:::::On::::::::::::::nny:::::y       y:::::y    x:::::x  x:::::x  
O:::::O     O:::::Onn:::::::::::::::ny:::::y     y:::::y      x:::::xx:::::x   
O:::::O     O:::::O  n:::::nnnn:::::n y:::::y   y:::::y        x::::::::::x    
O:::::O     O:::::O  n::::n    n::::n  y:::::y y:::::y          x::::::::x     
O:::::O     O:::::O  n::::n    n::::n   y:::::y:::::y           x::::::::x     
O::::::O   O::::::O  n::::n    n::::n    y:::::::::y           x::::::::::x    
O:::::::OOO:::::::O  n::::n    n::::n     y:::::::y           x:::::xx:::::x   
 OO:::::::::::::OO   n::::n    n::::n      y:::::y           x:::::x  x:::::x  
   OO:::::::::OO     n::::n    n::::n     y:::::y           x:::::x    x:::::x 
     OOOOOOOOO       nnnnnn    nnnnnn    y:::::y           xxxxxxx      xxxxxxx
                                        y:::::y                                
                                       y:::::y                                 
                                      y:::::y                                  
                                     y:::::y                                   
                                    yyyyyyy                                    
                                                                               
                                                                               
""")

print(Fore.CYAN+"Type in the number among the list below :\n \n 1)-Password list \n 2)-Add Password Profile  \n" )


while True:
    a = input(Fore.YELLOW +"Onyx >>")
    if a== "2":

        # Data Gathering
        print(Fore.GREEN+"Your password profile will contain the following informations :\n -Name (Important for file Handeling) \n -website (optional) \n -password \n \n")
        
        Name = input(Fore.LIGHTMAGENTA_EX+"Enter the profile's name : ")

        Website = input(Fore.LIGHTMAGENTA_EX+"Enter the website's url (Leave empty if there are none) : ")
        if Website == "":
            Website = "None"
        
        Username = input(Fore.LIGHTMAGENTA_EX+"Enter the username or email matching the website(Leave blank if unncessary)")
        if Username == "":
            Username="None"

        Password = input(Fore.LIGHTMAGENTA_EX+"Enter your password (Leave blank if you want ot automatically generate one : ")
        if Password == "":
            Password = str(P.GeneratePassword())

        

        #WriteData

        data = {
            f"{Name}" : {

                "Website" : f"{Website}",
                "Username" : f"{Username}",
                "Password" : f"{Password}"


            }
        }

        with open(f"Onyxes\{Name}.json","w+") as PFile:
            MSG = PFile.read().encode()
            NAME = PFile.name
            json.dump(data,PFile)
            PFile.close()
        
        #Encryption 

        Op.Encrypt(Name,MSG)

    elif a== "1":
        for filename in os.listdir('Onyxes'):
            with open(os.path.join('Onyxes',filename),"r+") as f:
                KID = f.read(4)
            
                with open(f"C:\Ony\{KID}.key","rb") as KFile:
                    DKEY = KFile.read(44)
                    # print(DKEY)
                    Fname = KFile.read().replace(DKEY,b'')

                # OFileName = (Fernet(open(f"C:\Ony\{KID}.key","rb").read()).decrypt(Fname))
                OFileName = Fernet(DKEY).decrypt(Fname)
                print(OFileName.decode())
            

            with open(f"Onyxes\{Fname}.key","rb") as DFile:
                print(DFile.read(4))
                content = DFile.read().replace(DFile.read(4),b'')
                print(content.decode())
                DecryptedContent = (Fernet(DKEY)).decrypt(content)
                print("Decrypted : ")
                print(DecryptedContent.decode())
             
    
    elif a=="exit":
        break
    
    else :
        print(Fore.RED+"Error : Invalid command entered")



