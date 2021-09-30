import smtplib
from email.message import EmailMessage
from os import system
from time import sleep
import platform
import sys

# függvények, parancsikonok (shortcuts)
if platform.system() == "Windows":
    # pre-defining the clear function
    def clear():
        system("cls")
else:
    # pre-defining the clear function
    def clear():
        system("clear")

def en():
    clear()
    def idiota(var):
        if var != "":
            print("PRESSING ENTER WOULD'VE BEEN ENOUGH, BUT OK!")
            sleep(0.69420)
        clear()
    # megjegyzések a felhasználó számára
    print("DISCLAIMER: READ THE README.MD DOCUMENT BEFORE USING THIS PROGRAM!")
    print("ALSO, THIS PROGRAM IS COMPLETELY HARMLESS & THE OPEN SOURCE CAN BE FOUND ON GITHUB!")
    print("PRESS ENTER TO CONTINUE")
    eula = input("")
    idiota(eula)

    # cimző paraméterei
    def cimzo():
        try:
            cimzo.cimzo_felhasznalonev = input("username: ")
            cimzo.cimzo_jelszo = input("password: ")
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(cimzo.cimzo_felhasznalonev, cimzo.cimzo_jelszo)
        except smtplib.SMTPAuthenticationError as auth:
            clear()        
            print("ERROR: INVALID USERNAME / PASSWORD\nERROR: "+str(auth)+"\n")
            cimzo()
        except TypeError as typeerror:
            clear()
            print("ERROR: EMPTY USERNAME\nERROR: "+str(typeerror)+"\n")
            cimzo()    
        clear()
        print("SUCCESSFUL LOGIN")
    cimzo()
    cimzo_felhasznalonev = cimzo.cimzo_felhasznalonev
    cimzo_jelszo = cimzo.cimzo_jelszo
    cimzo_nev = input("\n#MAIL FROM:\n")

    # levél paraméterei
    end = "¤"
    i = 0
    level_targy = input("\n#LETTER SUBJECT\n")
    level_tartalom = []
    def main():
        main.level_tartalom = input("\n#LETTER CONTENT\n")
        main.i = 2
        main.kilépés = False
        def ujsor():
            if "¤" in main.level_tartalom:
                main.level_tartalom = list(main.level_tartalom)
                main.level_tartalom[-1] = "\n"
                while main.kilépés != True:
                    ujsor_var = input()
                    main.i += 1
                    main.level_tartalom.extend(ujsor_var)
                    if "¤" in ujsor_var:
                        ujsor()
                    else:
                        main.kilépés = True
        ujsor()
    main()
    level_tartalom = "".join(main.level_tartalom)
    print()

    def kuldes():
        # címzett
        cimzett_email = input("#MAIL TO\n")
        while cimzett_email == "":
            clear()
            print("SUCCESSFUL LOGIN!")
            print("\n#MAIL FROM\n"+cimzo_nev)
            print("\n#LETTER SUBJECT\n"+level_targy)
            print("\n#LETTER CONTENT\n"+level_tartalom)
            print("\nERROR: EMPTY ADDRESSEE, TRY AGAIN!")
            cimzett_email = input("#MAIL TO\n")

        # email objektívum létrehozása
        email = EmailMessage()
        # Név megadása a címző részéről
        email["from"] = cimzo_nev
        # Címezett megadása
        email["to"] = cimzett_email
        # Levél tárgyának megadása
        email["subject"] = level_targy
        email.set_content(level_tartalom)

        # Hozzon létre STMP szervert
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            # Biztonságosan rácsatlakozzon a szerverre
            smtp.starttls()
            # Belépés felhasználónév és jelszóval egy bábu gmailbe.
            # https://myaccount.google.com/lesssecureapps <-- feltétlen be kell kapcsolni.
            smtp.login(cimzo_felhasznalonev, cimzo_jelszo)
            # Levél küldése
            try:
                smtp.send_message(email)
            except smtplib.SMTPRecipientsRefused:
                clear()
                print("SUCCESSFUL LOGIN!")
                print("\n#MAIL FROM\n"+cimzo_nev)
                print("\n#LETTER SUBJECT\n"+level_targy)
                print("\n#LETTER CONTENT\n"+level_tartalom)
                print("ERROR: INVALID ADDRESSSEE E-MAIL.")
                kuldes()
            else:
                print("\nTHE MESSAGE HAS BEEN SENT.")
                utsolepes = input("PRESS ENTER TO EXIT\n")
                idiota(utsolepes)
    kuldes()
def hu():
    clear()
    def idiota(var):
        if var != "":
            print("Elég lett volna egy entert is nyomni, de mindegy...")
            sleep(0.69420)
        clear()
    # megjegyzések a felhasználó számára
    print("FIGYELEM: OLVASD EL A README.MD DOKUMENTUMOT MIELŐTT HASZNÁLNÁD A PROGRAMOT!")
    print("ILLETVE, EZ A PROGRAM TELJES MÉRTÉKBEN ÁRTATLAN ÉS NYÍLT FORRÁSA MEGTALÁLHATÓ GITHUBON!")
    print("ÜSSE LE AZ ENTER BILLENTYŰZETET HA FOLYTATNI KÍVÁNJA.")
    eula = input("")
    idiota(eula)

    # cimző paraméterei
    def cimzo():
        try:
            cimzo.cimzo_felhasznalonev = input("Felhasználónév: ")
            cimzo.cimzo_jelszo = input("Jelszó: ")
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(cimzo.cimzo_felhasznalonev, cimzo.cimzo_jelszo)
        except smtplib.SMTPAuthenticationError as auth:
            clear()        
            print("ERROR: HIBÁS FELHASZNÁLÓNÉV / JELSZÓ\nERROR: "+str(auth)+"\n")
            cimzo()
        except TypeError as typeerror:
            clear()
            print("ERROR: ÜRES FELHASZNÁLÓNÉV\nERROR: "+str(typeerror)+"\n")
            cimzo()    
        clear()
        print("SIKERES BEJELENTKEZÉS!")
    cimzo()
    cimzo_felhasznalonev = cimzo.cimzo_felhasznalonev
    cimzo_jelszo = cimzo.cimzo_jelszo
    cimzo_nev = input("\n#CÍMZŐ NEVE\n")

    # levél paraméterei
    end = "¤"
    i = 0
    level_targy = input("\n#LEVÉL TÁRGYA\n")
    level_tartalom = []
    def main():
        main.level_tartalom = input("\n#LEVÉL TARTALMA\n")
        main.i = 2
        main.kilépés = False
        def ujsor():
            if "¤" in main.level_tartalom:
                main.level_tartalom = list(main.level_tartalom)
                main.level_tartalom[-1] = "\n"
                while main.kilépés != True:
                    ujsor_var = input()
                    main.i += 1
                    main.level_tartalom.extend(ujsor_var)
                    if "¤" in ujsor_var:
                        ujsor()
                    else:
                        main.kilépés = True
        ujsor()
    main()
    level_tartalom = "".join(main.level_tartalom)
    print()

    def kuldes():
        # címzett
        cimzett_email = input("#CÍMZETT\n")
        while cimzett_email == "":
            clear()
            print("SIKERES BEJELENTKEZÉS")
            print("\n#CÍMZŐ NEVE\n"+cimzo_nev)
            print("\n#LEVÉL TÁRGYA\n"+level_targy)
            print("\n#LEVÉL TARTALMA\n"+level_tartalom)
            print("\nERROR: ÜRES CÍMZETT")
            cimzett_email = input("#CÍMZETT\n")

        # email objektívum létrehozása
        email = EmailMessage()
        # Név megadása a címző részéről
        email["from"] = cimzo_nev
        # Címezett megadása
        email["to"] = cimzett_email
        # Levél tárgyának megadása
        email["subject"] = level_targy
        email.set_content(level_tartalom)

        # Hozzon létre STMP szervert
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            # Biztonságosan rácsatlakozzon a szerverre
            smtp.starttls()
            # Belépés felhasználónév és jelszóval egy bábu gmailbe.
            # https://myaccount.google.com/lesssecureapps <-- feltétlen be kell kapcsolni.
            smtp.login(cimzo_felhasznalonev, cimzo_jelszo)
            # Levél küldése
            try:
                smtp.send_message(email)
            except smtplib.SMTPRecipientsRefused:
                clear()
                print("SIKERES BEJELENTKEZÉS")
                print("\n#CÍMZŐ NEVE\n"+cimzo_nev)
                print("\n#LEVÉL TÁRGYA\n"+level_targy)
                print("\n#LEVÉL TARTALMA\n"+level_tartalom+"\n")
                print("ERROR: A címzett e-mail címe érvénytelen!")
                kuldes()
            else:
                print("\nÜzenet kézbesítve.")
                utsolepes = input("Nyomd meg az ENTERT a kilépéshez.\n")
                idiota(utsolepes)
                sys.exit()
    kuldes()
    
clear()

def lang():
    lang_input = input("Welcome - Üdv\n[1] - English\n[2] - Hungarian\nYou - Te: ")
    if lang_input !="1" and lang_input !="2":
        clear()
        print("ERROR: EMPTY ANSWER, TRY AGAIN!")
        lang()
    if lang_input == "1":
        en()
    if lang_input == "2":
        hu()
lang()
