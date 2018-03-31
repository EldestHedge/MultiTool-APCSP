#Mathamatical multitool
#Made by Lucas Brattinga and in collaboration with Cameron Lewis


print("                          ")
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

class MainMenu():
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

    multi = 0

    selection = input("Choose an option: ")

    while True:

        if selection == "1":
                multi = 1
                print ("[Unit Convirter]")
                break

        elif selection == "2":
                multi = 2
                print ("[Basic Calculator] ")
                break

        elif selection == "3":
                multi = 3
                print(" [Mortgage Calculator] ")
                break

        elif selection == "4":
                multi = 4
                print (" [Area of Shapes]")
                break


        elif selection == "5":
                multi = 5
                print ("[Meal Price]")
                break

        elif selection == "6":
                multi = 6
                print ("[Help]")
                break

        elif selection == '7':
                multi = 7
                break

        elif selection == '8':
                break

        else:
                print("[!]Error unknown character")

if MainMenu.multi == 1:
    print("In developement")

elif MainMenu.multi == 2:
        #Basic Calculator V1

    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")

    class Topporator:
        def add(x,y):
            return x + y

        def subtract(x,y):
            return x - y

        def multi(x,y):
            return x * y

        def subtr(x,y):
            return x / y


    opporation = input("Choose an opporator (Only numbers 1-4): ")

    num1 = input("Number1: ")
    num2 = input("Number2: ")

    if opporation == '1':
        print (Topporator.add(float(num1),float(num2)))

    elif opporation == '2':
        print (Topporator.subtract(float(num1),float(num2)))

    elif opporation == '3':
        print (Topporator.multi(float(num1),float(num2)))

    elif opporation == '4':
        print (Topporator.subtr(float(num1),float(num2)))

elif MainMenu.multi == 3:
    print("In developement")

elif MainMenu.multi == 4:
    print("In developement")

elif MainMenu.multi == 5:
    print("In developement")

elif MainMenu.multi == 6:
    helptxt = open("Help.txt")
    print(helptxt.read())

elif MainMenue.multi == 7:
    credits_txt = open("Credits.txt")
    print(credits_txt.read())
