def print_multiplication_table(m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            result = i * j
            print(result," | ", end="")
        print()

x = int(input("Please Enter Row Number: "))
y = int(input("Please Enter Column Number: "))
print_multiplication_table(x, y)
