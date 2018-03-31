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
        print "Area of the circle is:"+ a_circle

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