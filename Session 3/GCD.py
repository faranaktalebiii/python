num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(min(num1, num2), 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        break

print("The GCD of the two numbers is:", gcd)
