# عدد n را از کاربر دریافت کنید
n = int(input("Please Enter Number: "))

# رشته‌ی حاوی الگوی مار را ذخیره می‌کند
snake_pattern = ""

# ساختن الگوی مار راه‌راه
for i in range(n):
    if i % 2 == 0:
        snake_pattern += "*"
    else:
        snake_pattern += "#"

# چاپ الگوی مار
print(snake_pattern)