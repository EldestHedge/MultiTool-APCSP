def PriceCalc():
    subtotal = float(input("Subtotal: "))
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
    
    if again == 'y':
        PriceCalc()
    elif again == 'n':
        Main()
        MMenu()
    else:
        print "[!] Error! Invalid input!"
        print 'Please only use characters "y" and "n" '
        PriceCalc()