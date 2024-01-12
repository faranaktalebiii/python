def print_diamond(k):
    if k % 2 == 0:
        k += 1

    for i in range(1, k+1, 2):
        spaces = (k - i) // 2
        print(' ' * spaces + '*' * i)

    for i in range(k-2, 0, -2):
        spaces = (k - i) // 2
        print(' ' * spaces + '*' * i)

k = int(input("Please Enter Odd Number: "))


print_diamond(k)
