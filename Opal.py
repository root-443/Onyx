from cryptography.fernet import Fernet
import json, os, random

class Opal:
    def __init__(self):
        pass

    def Encrypt(self, Name, MSG):
        key = Fernet.generate_key()
        F = Fernet(key)
        ID = str(random.randint(1000,9999))

        with open(f"C:\Ony\{ID}.key","wb") as KFile: #Kfile = KeyFile
            # print(key)
            KFile.write(key)
        
        EncName = F.encrypt(Name.encode()) # Name : FileName

        os.rename(f"Onyxes\{Name}.json", f"Onyxes\{Name}.key")

        #Encrypt File
        #L'ID sera dans les 4 premiers caractère du fichier
        
        with open(f"Onyxes\{Name}.key","w") as EFile:
            EFile.write(ID)
            EFile.close()
        


        with open(f"Onyxes\{Name}.key","ab") as EFile:
            EFile.write(F.encrypt(MSG))
            EFile.close()
        
        os.rename(f"Onyxes\{Name}.key", f"Onyxes\{EncName}.key")

        #On ajoute Le nom du fichier crypté à la fin du KeyFile

        with open(f"C:\Ony\{ID}.key","ab") as KFile:
            KFile.write(EncName)
    



        

    
        
    