import os

def Main():
    print "Mathematicl Multitool"
    print "Made by Cam Lewis"
    print "Collaborated with Lucas Brattinga"

    print ""
    print " '||\   /||`           ||    '||                                 ||                       '||`    '||\   /||'          '||`   ||           ||                  '||`"
    print "  ||\\.//||            ||     ||                                 ||     ''                 ||      ||\\.//||            ||    ||     ''    ||                   || "
    print "  ||     ||   '''|.  ''||''   ||''|, .|''|, '||),,(|,   '''|.  ''||''   ||  .|'',  '''|.   ||      ||     ||  '||  ||`  ||  ''||''   ||  ''||''  .|''|, .|''|,  || "
    print "  ||     ||  .|''||    ||     ||  || ||..||  || || ||  .|''||    ||     ||  ||    .|''||   ||      ||     ||   ||  ||   ||    ||     ||    ||    ||  || ||  ||  || "
    print " .||     ||. `|..||.   `|..' .||  || `|...  .||    ||. `|..||.   `|..' .||. `|..' `|..||. .||.    .||     ||.  `|..'|. .||.   `|..' .||.   `|..' `|..|' `|..|' .||. "
    print ""

class MainMenu:
    startup = True

    def MMenu():
        menu = {}
        menu['1'] = "Temperature Converter"
        menu['2'] = "Calculator"
        menu['3'] = "Area of Shapes"
        menu['4'] = "Meal Price Calculator"
        menu['5'] = "Help"
        menu['6'] = "Credits"
        menu['7'] = "Exit"

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
        elif selection == "7":
            multi = 7
            os.system('cls')
            break 

        else:
            print("[1}Error unknown input, only use characters 1 through 6")

if multi == 1:
    #Temperature Converter
    Main()
    print("Temperature Converter")

    def TempConverter():
        def TemperatureScript():
            print ("[1] Celsius to Fahrenheit")
            print ("[2] Celsius to Kelvin")
            print ("[3] Fahrenheit to Celsius")
            print ("[4] Fahrenheit to Kelvin")
            print ("[5] Kelvin to Celsius")
            print ("[6] Kelvin to Fahrenheit")
            print ("[7] Back to Main Menu")

        TemperatureScript()
        print ("")
        
        TempInput = int(input("Select an option: "))

        if TempInput == 1:
            #insert Celsius to Fahrenheit
            CTemp = float(input("Degrees Celsius: "))
            Far = CTemp * 1.8 + 32

            print (str(CTemp) + " degrees Celsius = " + str(Far) + " degrees Fahrenheit")
            
        if TempInput == 2:
            #insert Celsius to Kelvin
            CTemp = float(input("Degrees Celsius: "))
            Kel = CTemp + 273.15

            print (str(CTemp) + " degrees Celsius = " + str(Kel) + " degrees Kelvin")

        if TempInput == 3:
            #insert Fahrenheit to Celsius
            FTemp = float(input("Degrees Fahrenheit: "))
            Cel = (FTemp - 32) / 1.8

            print (str(FTemp) + " degrees Fahrenheit = " + str(Cel) + " degrees Celsius")

        if TempInput == 4:
            #insert Fahrenheit to Kelvin
            FTemp = float(input("Degrees Fahrenheit: "))
            Kel = (FTemp + 495.67) * (5/9)

            print (str(FTemp) + " degrees Fahrenheit = " + str(Kel) + " degrees Kelvin")

        if TempInput == 5:
            #insert Kelvin to Celsius
            KTemp = float(input("Degrees Kelvin: "))
            Cel = KTemp - 273.15
            
            print (str(KTemp) + " degrees Kelvin = " + str(Cel) + " degrees Celsius")

        if TempInput == 6:
            #insert Kelvin to Fahrenheit
            KTemp = float(input("Degrees Kelvin: "))
            Far = KTemp * 1.8 - 495.67

            print (str(KTemp) + " degrees Kelvin = " + str(Far) + " degrees Fahrenheit")

        if TempInput == 7:
            #BackButton
            os.system('cls')
            Main()
            MainMenu.MMenu()


        TempConverter()

if multi == 2:
    #Calculator
    Main()
    print("[Basic Calculator]")
    
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

if multi == 3:
    #AREA OF SHAPES

    print "[1] Perimeter of a Quadrilateral"
    print "[2] Volume of a Box"
    print "[3] Area of a Circle"
    print "[4] Area of a Quadrilateral"
    print "[5] Circumference of a Circle"
    print "[6] Area of a Trapezoid"
    print "[7] Area of a Cylinder"
    print ""

    ask = input("Which shape would you like to find the area of? ")

    class shapes:

        def perimeter(base, height):
            perimeter = (base + height) * 2
            print "Perimeter: " + str(perimeter)

        def volume(base, height, length):
            volume = base * height * length
            print "Volume: " + str(volume)

        def a_circle(radius):
            a_circle = (radius**2) * 3.14
            print "Area of the circle is:" + a_circle

        def a_quad(base, height):
            a_quad = base * height
            print "The area of the quadrilateral is: " + a_quad

        def cirum(radius):
            circum = 2 * 3.14 * radius
            print "The cirumference of the circle is: " + cirum

        def a_trap(first_base, second_base, height):
            a_trap = (.5 * (first_base + second_base) * height)
            print "The area of the trapezoid is: " + a_trap

        def a_cylinder(height, radius):
            a_cylinder = #Insert formula

    if ask == "1":
        print (shapes.perimeter)

    if ask == "2":
        print (shapes.volume)

    if ask == "3":
        print (shapes.a_circle)

    if ask == "4":
        print (shapes.a_quad)

    if ask == "5":
        print (shapes.circum)

    if ask == "6":
        print (shapes.a_trap)

    if ask == "7":
        print (shapes.a_cylinder)
    if ask == "8":
        #Go back

if multi == 4:
    def PriceCalc():
        subtotal = float(input("Price: "))
        tip = float(input("Tip Percentage: "))
        tax = subtotal * 0.06
        tip = (tip / 100) * subtotal
        total = subtotal + tax + tip
        
        print ""
        print "Subtotal: $" + str(subtotal)
        print "Tax: $" + str(tax)
        print "Tip: $" + str(tip)
        print "Total price: $" + str(total)
        
        print ""
        again = str(input("Would you like to calculate another price? [y/n] "))
        
        if again == "y":
            PriceCalc()
        elif again == "n":
            Main()
            MainMenu.MMenu()
        else:
            print "[!] Error! Invalid input!"
            print 'Please only use characters "y" and "n" '
            PriceCalc()

    PriceCalc()
if multi == 5:
    #oof

if multi == 6:
    #oof

if multi == 7:
    #oof