import time
import os 
from os import *
import colorama

a = 0
b = 3
c = 0
mdp = "trax"
max = 3
true = "Correct", + os.system('color 2')
false = "Incorrect", + os.system('color 4')

def connexion():
    while a != b:
        os.system('cls')
        print(colorama.Fore.LIGHTMAGENTA_EX + """
     ██░ ██  ▄████▄   ██ ▄█▀   ▄▄▄█████▓ ██▀███   ▄▄▄      ▒██   ██▒
    ▓██░ ██▒▒██▀ ▀█   ██▄█▒    ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒▒ █ █ ▒░
    ▒██▀▀██░▒▓█    ▄ ▓███▄░    ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ░░  █   ░
    ░▓█ ░██ ▒▓▓▄ ▄██▒▓██ █▄    ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██  ░ █ █ ▒ 
    ░▓█▒░██▓▒ ▓███▀ ░▒██▒ █▄     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ▒██▒
    ▒ ░░▒░▒░ ░▒ ▒  ░▒ ▒▒ ▓▒     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▒ ░ ░▓ ░
    ▒ ░▒░ ░  ░  ▒   ░ ░▒ ▒░       ░      ░▒ ░ ▒░  ▒   ▒▒ ░░░   ░▒ ░
    ░  ░░ ░░        ░ ░░ ░      ░        ░░   ░   ░   ▒    ░    ░  
    ░  ░  ░░ ░      ░  ░                  ░           ░  ░ ░    ░  
            ░                                                       
    """ + colorama.Style.RESET_ALL)
        time.sleep(1)
        print(colorama.Fore.BLUE + "[1] SITE WEB 🌐")
        time.sleep(0.3)
        print(colorama.Fore.YELLOW + "[2] Projet Python 📁")
        time.sleep(0.3)
        print(colorama.Fore.GREEN + "[3] Python Hacking 🐍")
        time.sleep(0.3)
        print(colorama.Fore.RED + "[4] dossier secret ⛔")
        time.sleep(1)
        print(colorama.Fore.WHITE + "\nChoisissez un numéro")
        choix = input(">>> ")
        if(choix == '1'):
            time.sleep(1)
            os.system('cls')
            os.system('color 5')
            print("Lancement...")
            time.sleep(1)
            os.system("python c:/Users/bmael/OneDrive/Bureau/code/app/hcktrax/site/site_web.py")
            break
        elif(choix == '2'):
            time.sleep(1)
            os.system('cls')
            os.system('color 5')
            print("Lancement...")
            time.sleep(1)
        elif(choix == '3'):
            time.sleep(1)
            os.system('cls')
            os.system('color 5')
            print("Lancement...")
            time.sleep(1)
        elif(choix == '4'):
            time.sleep(1)
            os.system('cls')
            os.system('color 5')
            print("Lancement...")
            time.sleep(1)
        else:
            os.system('cls')
            time.sleep(1)
            print(colorama.Fore.RED + " [!] Veuillez choisir un nombre. \n Exemple : 1")
            time.sleep(1)

while a != b:
    os.system('cls')
    os.system('color 9')
    a += 1
    c += 1
    max -= 1
    print("BIENVENUE ♾️")
    time.sleep(1)
    if(c == 0):
        tent = f"tentative({c})"
    elif(c == 1):
        tent = f"tentative({c})"
    else:
        tent = f"tentatives({c})"
    if(tent == 1):
        max = f"max({max})"
    elif(tent == 2):
        max = f"max({max})"
    elif(tent == 3):
        max = f"max({max})"
    print("Entrez votre mot de passe pour vous connecter🔑 => ", (tent), {max})
    lemdp = input(">>> ")
    if(lemdp == mdp):
        os.system('cls')
        print("password :")
        time.sleep(0.5)
        os.system('cls')
        os.system('color 2')
        print("password : Correct")
        time.sleep(2)
        connexion()
        break
    else:
        os.system('cls')
        print("password :")
        time.sleep(0.5)
        os.system('cls')
        os.system('color 4')
        print("password : Incorrect")
        time.sleep(2)
        os.system('cls')
    if(a == b):
        os.system('color 4')
        print("Trop de tentatives [❗ARRET DU PROGRAMME❗]")
        time.sleep(3)
        os.system('cls')
        os.system('color 7')
        print("😒😒😒😒😒")
        break
    


