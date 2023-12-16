Weight = float (input ("Please Enter Your Weight (Based on kg): "))
Height = float (input("Please Enter Your height (Base on m): "))
BMI = Weight/ (Height**2)
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal Weight")
elif BMI > 24.9 and BMI <= 29.9:
    print ("Over Weight")
elif BMI >= 30 and BMI <= 34.9:
    print ("Obesity")
elif BMI > 35:
    print ("Extreme Obesity")
    