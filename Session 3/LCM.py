num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(max(num1, num2), num1 * num2 + 1, max(num1, num2)):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break

print("The LCM of the two numbers is:", lcm)
