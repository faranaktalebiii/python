side1= float (input("Please Enter the size of the first Side: "))
side2= float (input("Please Enter the size of the Second Side: "))
side3= float (input("Please Enter the size of the Third Side: "))
if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print ("It is possible to draw a triangle with these dimensions")
else:
    print ("It is NOT possible to draw a triangle with these dimensions")