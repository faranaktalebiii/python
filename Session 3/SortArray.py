input_str = input("Please Enter your Array separated by space: ")  # دریافت رشته از کاربر
input_array = list(map(int, input_str.split()))  # تبدیل رشته به لیست اعداد
# بررسی مرتب بودن آرایه
is_sorted = True
for i in range(len(input_array) - 1):
    if input_array[i] > input_array[i + 1]:
        is_sorted = False
        break

if is_sorted == True:
    print("The Array sort is  Descending.")
else:
    print("The Array is NOT Sort descending.")