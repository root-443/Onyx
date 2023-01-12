from colorama import Fore, Back, Style
import Opal,PGen

#Opal is the Utility class and Pgen is the class of the password generator
#Defining an instance for Opal and Pgen :
OPAL = Opal.Opal()
PASSWORD_GENERATOR= PGen.PGen()

# A nice intro
OPAL.intro()

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
            Password = str(PASSWORD_GENERATOR.GeneratePassword())
        
# Writing data in a dictionnary
        data = {
            
                
                "Name"    : f"{Name}",
                "Website" : f"{Website}",
                "Username" : f"{Username}",
                "Password" : f"{Password}"


            
        }

        OPAL.encrypt(Name,data)
    
    elif a=="1":
        print("1 pressed")
        OPAL.decrypt()
    
    elif a=="exit":
        break

    else:
        print(Fore.RED + "Invalid Command")
        





