import random
n = int(input ("Please Enter Your Number: "))
range_start = 1  # شروع محدوده اعداد تصادفی
range_end = n + 1  # پایان محدوده اعداد تصادفی

random_numbers = []  # آرایه برای نگهداری اعداد تصادفی غیر تکراری

while len(random_numbers) < n:
    num = random.randint(range_start, range_end)  # ایجاد عدد تصادفی در محدوده
    if num not in random_numbers:  # بررسی تکراری نبودن عدد
        random_numbers.append(num)

print("Random Array is:", random_numbers)
