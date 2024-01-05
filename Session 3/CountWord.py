# دریافت جمله از کاربر
sentence = input("Please Enter Your Sentence: ")

# شمارش تعداد کلمات در جمله
word_count = 0
is_word = False  # شرطی برای بررسی اینکه آیا در حال خواندن یک کلمه هستیم یا خیر

# حلقه برای بررسی هر حرف در جمله
for char in sentence:
    # اگر حرف یافت شده یک حرف فاصله باشد، تعداد کلمات افزایش می‌یابد
    if char == ' ':
        if is_word:
            word_count += 1
            is_word = False
    else:
        is_word = True

# بررسی آخرین کلمه در صورتی که جمله با کلمه ختم نشده باشد
if is_word:
    word_count += 1

# چاپ تعداد کلمات
print("Word count is:", word_count)
