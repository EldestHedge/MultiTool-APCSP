subtotal = float(input("Meal Price: "))
tax = subtotal * 0.06
tip = float(input("Tip: "))
total = subtotal + tax + tip

print "Subtotal: " + str(subtotal)
print "Tax: " + str(tax)
print "Tip: " + str(tip)
print "Total price: " + str(total)