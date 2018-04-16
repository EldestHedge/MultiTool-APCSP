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
        menu["[3]"] = ("Area of Shapes")
        menu["[4]"] = ("Meal Price")
        menu["[5]"] = ("Help")
        menu["[6]"] = ("Credits")
        menu["[7]"] = ("Exit")

        choice = menu.keys()
        for row in choice:
                print (row, menu[row])
    MMenu()

    def SelectionSkript():
        selection = input("Choose an option: ")
        if selection == "1":
            Main()
            print("[Unit Convirter]")
            os.system('cls')
        elif selection == "2":   
            os.system('cls')
        elif selection == "3":
            os.system('cls')
        elif selection == "4":
            os.system('cls')
        elif selection == "5":
            os.system('cls')
        elif selection == '6':
            os.system('cls')
        else:
            print("[!]Error unknown input")
            os.system('cls')
    SelectionSkript()

MainMenu()

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
                MainMenu()
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

def HelpMenu():
    print("                        ~~~~~[Help]~~~~~")
    helptxt = open("Help.txt")
    print(helptxt.read())
    input()
HelpMenu()

def Credits():
    print("[Credits]")
    credits_txt = open("Credits.txt")
    print(credits_txt.read())
Credits()