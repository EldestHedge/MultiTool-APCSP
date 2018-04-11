#Mortgage Calculator
print("Basic Mortgage calculator")
print("[1]Mortgage Calculator")
print("[2]Instructions")
print("[3]Go Back")

choice = input(": ")
if choice == '1':
    class loans:
        def fixed():
            return("Test fixed")

        def intrest():
            print("Test intrest")

        def adjustable():
            print("Test adjustable")

    #loanammount = input("The loan ammount: ")
    #intrest_rate = input("Intrest rate: ")
    #noyrepay = input("Number of years to repay, the term:  ")

    print("Types of Loan")
    print("[1] Fixed-rate loan")
    print("[2] Intrest-only loan")
    print("[3] Adjustable loan")
    typeloan = input("Type of loan: ")

    if typeloan == '1':
        print (loans.fixed)

    elif typeloan == '2':
        print (loans.intrest)

    elif typeloan == '3':
        print (loans.interest)

elif choice == '2':
    print("Test2")
    #clear screen and print the instrictions,
    #at the end of the instructionshave an option to go back to the menue

elif choice == '3':
    print("Test3")
    #go back to the previous menue

else:
    print ("[!]Error only characters 1-3")
        #Start up the Mortgage skript fornm the begining
