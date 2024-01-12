def print_khayyam_triangle(n):
    for i in range(n):       
       
        for j in range(i + 1):
            print(choose(i, j), end=" ")

     
        for j in range(i):
            print(choose(i, i - j - 1), end=" ")

        print()

def choose(n, k):
    result = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

x = int(input("Please Enter Number: "))
print_khayyam_triangle(5)
