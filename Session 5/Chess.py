def print_chessboard(m, n):
    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("#", end="")
            else:
                print("*", end="")
        print()

x = int(input("Please Enter Row Number: "))
y = int(input("Please Enter Column Number: "))
print_chessboard(x, y)
