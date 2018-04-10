#Mathamatical multitool
#Made by Lucas Brattinga and in collaboration with Cameron Lewis
import os

def Main():

    print("")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("   M th m ti  l Multitool ")
    print("    X  X X  .X            ")
    print("    X  X X  .X            ")
    print("    .  X .  ..            ")
    print("    .  X .  ..            ")
    print("    .  X .  ..            ")
    print("    .  . .  ..            ")
    print("                          ")
    print("  Mathematical Multitool  ")
    print("    By: Lucas Brattinga   ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~ ")

Main()

class MainMenu():
    def MMenu():
        print("       [Main Menu]")
        menu = {}
        menu["[1]"] = ("Unit Convirter")
        menu["[2]"] = ("Calculator")
        menu["[3]"] = ("Mortgage Calculator")
        menu["[4]"] = ("Area of Shapes")
        menu["[5]"] = ("Meal Price")
        menu["[6]"] = ("Help")
        menu["[7]"] = ("Credits")
        menu["[8]"] = ("Exit")

        choice = menu.keys()
        for row in choice:
                print (row, menu[row])
    MMenu()
    multi = 0

    selection = input("Choose an option: ")

    while True:

        if selection == "1":
                multi = 1
                os.system('cls')
                break
        elif selection == "2":
                multi = 2
                os.system('cls')
                break
        elif selection == "3":
                multi = 3
                os.system('cls')
                break
        elif selection == "4":
                multi = 4
                os.system('cls')
                break
        elif selection == "5":
                multi = 5
                os.system('cls')
                break
        elif selection == "6":
                multi = 6
                os.system('cls')
                break
        elif selection == '7':
                os.system('cls')
                multi = 7
                break
        else:
                print("[!]Error unknown input")
                os.system('cls')
                input()
                MMenu()
                break

MainMenu()

if MainMenu.multi == 1:
    Main()
    print("[Unit Convirter]")
    input()

elif MainMenu.multi == 2:
    Main()
    print("     [Basic Calculator] ")
        #Basic Calculator V1
    def CalculatorScript():
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")
        print("[5] Back")

        class Topporator:
            def add(x,y):
                return x + y

            def subtract(x,y):
                return x - y

            def multi(x,y):
                return x * y

            def subtr(x,y):
                return x / y

        opporation = input("Choose an option: ")

        if opporation == '1':
            num1 = input("Number1: ")
            num2 = input("Number2: ")
            print (Topporator.add(float(num1),float(num2)))

        elif opporation == '2':
            num1 = input("Number1: ")
            num2 = input("Number2: ")
            print (Topporator.subtract(float(num1),float(num2)))

        elif opporation == '3':
            num1 = input("Number1: ")
            num2 = input("Number2: ")
            print (Topporator.multi(float(num1),float(num2)))

        elif opporation == '4':
            num1 = input("Number1: ")
            num2 = input("Number2: ")
            print (Topporator.subtr(float(num1),float(num2)))

        elif opporation == '5':
                os.system('cls')
                Main()
                MainMenu.MMenu()
                #working back button^
        else:
            print ("")
            print ("[!]Error")
            print ("")
            input()
            os.system('cls')
            Main()
            print("     [Basic Calculator] ")
            CalculatorScript()
    CalculatorScript()


elif MainMenu.multi == 3:
    print(" [Mortgage Calculator] ")

elif MainMenu.multi == 4:
    print(" [Area of Shapes]")
elif MainMenu.multi == 5:
    print("[Meal Price]")

elif MainMenu.multi == 6:
    print("                        ~~~~~[Help]~~~~~")
    helptxt = open("Help.txt")
    print(helptxt.read())
    input()

elif MainMenu.multi == 7:
    print("[Credits]")
    credits_txt = open("Credits.txt")
    print(credits_txt.read())
