import math
print ("Welcome To my Calculator")
print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print ("5. For Other Option Please Enter 5 (sqrt, sin, cos, tan, cot, factorial):")
print ("Please Enter Your Choice: ")
userinput = int(input ())
if userinput == 1 or userinput == 2 or userinput == 3 or userinput == 4:
    num1 = float (input("Plaese Enter Your First Number: "))
    num2 = float (input("Plaese Enter The Second One: "))
    if userinput == 1:
        Result = num1 + num2
    elif userinput == 2:
        Result = num1 - num2
    elif userinput == 3:
        Result = num1 * num2
    elif userinput == 4 and num2 == 0:
        Result = "Can not Calculate "
    elif userinput == 4:
        Result = num1 / num2
elif userinput == 5:
    print ("6. To Calculate sqrt:")
    print ("7. To Calculate sin:")
    print ("8. To Calculate cos:")
    print ("9. To Calculate tan:")
    print ("10. To Calculate cot:")
    print ("11. To Calculate factotial:")
    userinput2= int(input("Please Enter your Choice: "))
    num3 = int(input("Please Enter Your Number: "))
    if userinput2 == 6:
        Result = math.sqrt(num3)
    elif userinput2 == 7:
        Radian = num3 * 180 / math.pi
        Result = math.sin(Radian)
    elif userinput2 == 8:
        Radian = num3 * 180 / math.pi
        Result = math.cos(Radian)
    elif userinput2 == 9:
        Radian = num3 * 180 / math.pi
        Result = math.tan(Radian)
    elif userinput2 == 10:
        Radian = num3 * 180 / math.pi
        Result = math.cos(Radian)/math.sin(Radian)
    elif userinput2 == 11:
        Result = math.factorial(num3)
print(Result)