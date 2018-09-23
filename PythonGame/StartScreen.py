import sys
import os
import cmd
import time
import random
import textwrap

#sets the consol window size
os.system("mode con: cols=100 lines=40")

#-Start Screen Logo-#
def StartLogo():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print ("            OooOOo.               o                       o      'O                o       ")
    print ("            O     `O             O                        O       o               O        ")
    print ("            o      O         O   o                        o       O               o    O   ")
    print ("            O     .o        oOo  O                        o       o               O   oOo  ")
    print ("            oOooOO'  O   o   o   OoOo. .oOo. 'OoOo.       O      O' .oOoO' O   o  o    o   ")
    print ("            o        o   O   O   o   o O   o  o   O       `o    o   O   o  o   O  O    O   ")
    print ("            O        O   o   o   o   O o   O  O   o        `o  O    o   O  O   o  o    o   ")
    print ("            o'       `OoOO   `oO O   o `OoO'  o   O         `o'     `OoO'o `OoO'o Oo   `oO ")
    print ("                         o                                                                 ")
    print ("                      OoO'                                                                 ")
    print ("                                                 By Lucas ")
    print("")
    print("")
    print("")
    print("")
StartLogo()

#-Main Menue-#
def MainMenuSelection():
    print('====================================================================================================')
    print("                                             [1]Start game")
    print("                                             [2]How to play")
    print("                                             [3]Settings(Comming soon)")
    print("                                             [4]Quit game")
    print('====================================================================================================')

    STGL = ["Start game", "start game", "start", "Start", str(1)]
    HTPL = ["How to play", "how to play", str(2)]
    S = ['Settings', 'settings', str(3)]
    QGL = ["Quit", "Quit game", "quit", "quit game", str(4)]

    choice = input("~] ")

    if choice in STGL:
        print("Comming soon")
        time.sleep(2)
        os.system("cls")
        StartLogo()
        MainMenuSelection()
        #test = "starting game"
        #for character in test:           That text makes it procedurally generated
            #sys.stdout.write(character)
            #sys.stdout.flush()
            #time.sleep(0.10)

    elif choice in HTPL:
        htp_text = open("Help.txt")
        print(htp_text.read())
        print("returning to main menue, wait time 200ms")
        time.sleep(2)
        os.system("cls")
        StartLogo()
        MainMenuSelection()

    elif choice in S:
        print("[!]Comming soon")
        time.sleep(2)
        os.system("cls")
        StartLogo()
        MainMenuSelection()

    elif choice in QGL:
        def Quit_Menu():
            os.system("cls")
            StartLogo()
            print("Are you sure that you want to exit?(y/n)")
            quit_choice = input("~]")
            if quit_choice == "y":
                os.system("exit(0)")
                quit()
            elif quit_choice == "n":
                os.system("cls")
                StartLogo()
                MainMenuSelection()
            else:
                print("[!]Error invalid input please wait 100ms")
                time.sleep(1)
                os.system("cls")
                Quit_Menu()
        Quit_Menu()

    elif choice not in STGL or HTPL or QGL or S:
        print("[!]Error invalid input please wait 200ms")
        time.sleep(2)
        os.system("cls")
        StartLogo()
        MainMenuSelection()
MainMenuSelection()
