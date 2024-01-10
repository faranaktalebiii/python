import qrcode
name = input("Plaese Enter Your Name: ")
number = input("Plaese Enter Your Number: ")
name_number = name  +' '+ number
# print(name_number)
img = qrcode.make(name_number)
img.save(name_number + '.png')