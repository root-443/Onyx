from cryptography.fernet import Fernet #For encryption
from colorama import init, Fore, Back, Style # For colors
import pandas as pd #for display
import json, os, random,io,PGen



class Opal:
    init(convert=True)
    def __init__(self) :
        pass
    

    def intro(self):
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
        if not os.listdir('Obsidian'):
            while True:
                print("Looks like you're new here, let's set you a master password \n")
                PSWD = str(input(Fore.MAGENTA+ "Enter your master password : "))
                PSWD_CONFIRMED = str(input(Fore.MAGENTA+ "Confirm your master password : "))

                if PSWD == PSWD_CONFIRMED:
                    print(Fore.GREEN+ "Password saved ! You're all set")

                    PSWD_FERNET_KEY = Fernet.generate_key()
                    FERNET_PSWD = Fernet(PSWD_FERNET_KEY)
                    ENCRYPTED_PASSWORD = FERNET_PSWD.encrypt(bytes(PSWD,"utf-8"))
                    
                    with open("C:\Onyxx\WEEEEWILLWEEEEWILLROCKYOU.key'","wb") as KFILE:
                        KFILE.write(PSWD_FERNET_KEY)
                        KFILE.close()

                    with open("Obsidian\ALOUETTEGENTILLEALOUETTEALOUETTEJETEPLUMERAI.key","wb") as PFile:
                        PFile.write(ENCRYPTED_PASSWORD)
                        PFile.close()
                    break


                else:
                    print(Fore.RED+ "Your password doesn't match the confirmation")
        
        else:
            

            with open("C:\Onyxx\WEEEEWILLWEEEEWILLROCKYOU.key'","rb") as OKIFILE:
                PSWD_KEY = OKIFILE.read()
                OKIFILE.close()
            
            with open("Obsidian\ALOUETTEGENTILLEALOUETTEALOUETTEJETEPLUMERAI.key","rb") as OPFILE:
                DECRYPTED_PSWD = Fernet(PSWD_KEY).decrypt(OPFILE.read())
                # print(DECRYPTED_PSWD)
            
            while True:
                INPUT_PASSWORD = input(Fore.MAGENTA + "Enter your password : ")
                # print(INPUT_PASSWORD)
                if str(DECRYPTED_PSWD.decode()) == INPUT_PASSWORD:
                    print(Fore.GREEN + "***ACCESS GRANTED ***")
                    break
                else:
                    print(Fore.RED + "INCORRECT PASSWORD")
                



            


        print(Fore.CYAN+"Type in the number among the list below :\n \n 1)-Password list \n 2)-Add Password Profile  \n" )
    
    def encrypt(self,FileName:str,JSON_CONTENT:dict):
        

# Generating and Saving the key and generating file's ID

        key = Fernet.generate_key()
        ID = str(random.randint(1000,9999))
        fernet = Fernet(key)

        with open(f"C:\Ony\{ID}.key","ab") as KeyFile:
            KeyFile.write(key)
            KeyFile.close()

# writing, encrypting and renaming the bad boi

        with open(f"Onyxes\{FileName}.json","w+") as PasswordFile:
            json.dump(JSON_CONTENT,PasswordFile)
            PasswordFile.close()
        
        data = json.load(open(f"Onyxes\{FileName}.json","r+"))

        json_string = json.dumps(data) #converting the disctionnary into STR
        encrypted_json = fernet.encrypt(json_string.encode())

        with open(f"Onyxes\{FileName}.json","wb") as EncryptedPasswordFile:
            # print(encrypted_json)
            EncryptedPasswordFile.write(ID.encode() + encrypted_json)
            EncryptedPasswordFile.close()
        



        os.rename(f"Onyxes\{FileName}.json",f"Onyxes\{Fernet(key).encrypt(FileName.encode()).decode()}.json")

    # def display(self,json:dict):
    #     print(tabulate(dict))

    def decrypt(self):
        
        if not os.listdir('Onyxes'):
            print("You do not have any password saved yet")
        
        else:

            FILE_LIST = []
            JSON_LIST = []
            num = 0
            for filename in os.listdir('Onyxes'):
            
            
# Getting the ID
            
                with open(os.path.join('Onyxes',filename),"r+") as EFile:
                    FileID = EFile.read(4) # The first 4 caracters of the file are the ID
                    EFile.close()
                # print(FileID)

#Looking for The FileKey

                with open(f"C:\Ony\{FileID}.key","rb") as KeyFile:
                    FERNET_KEY = KeyFile.read()
                    KeyFile.close()
            # print(FERNET_KEY.decode())

                NEW_FERNET = Fernet(FERNET_KEY)
#Decrypting

                with open(f'Onyxes\{filename}',"r") as DecryptedFile:
                    Content = (DecryptedFile.read()).replace(FileID,"") #Remove the id from the string
                    DecryptedFile.close()

                DECRYPTED_CONTENT = (NEW_FERNET.decrypt(Content).decode()) 
                DECRYPTED_CONTENT_JSON = json.loads(DECRYPTED_CONTENT) #To display infos seperately
                JSON_LIST.append(DECRYPTED_CONTENT_JSON)
# df = pd.DataFrame(DECRYPTED_CONTENT_JSON)
# print(Fore.GREEN+" \n ***YOUR PASSWORD***")
# print(Fore.LIGHTGREEN_EX+df)
            num = 0
            print(Fore.RED + "CHOOSE THE DESIRED PROFILE")
        
            for a in JSON_LIST:
            
                print(Fore.GREEN + str(num)+ ") " + str(a['Name']) + "\n" )
                num= num+1
            while True:
                try:
                    CHOICE = int(input("Onyx >>"))
                    print(JSON_LIST[CHOICE])
                
                except(ValueError):
                    print(Fore.RED +"you must enter an integer matching the profile you want")
            
                df = pd.DataFrame(JSON_LIST[CHOICE], index=[0])
                print(Fore.GREEN+" \n ***YOUR PASSWORD***")
                print(df)
                break

        


           
            
        


        
            

