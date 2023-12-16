FirstName= input("Please Enter Your First Name: ")
LastName= input("Please Enter Your Last Name: ")
L1Score= int(input("Please Enter Your First Lesson Score: "))
L2Score= int(input("Please Enter Your Second Lesson Score: "))
L3Score= int(input("Please Enter Your Third Lesson Score: "))
average= (L1Score + L2Score + L3Score) / 3
if average >= 17:
    Grade = "Great"
elif average < 17 and average >= 12:
    Grade = "Normal"
elif average < 12:
    Grade = "Fail"
else:
    print("Your inputs is notv valid")
print (FirstName, LastName, "Your Average is:", average, )
print ("You Are", Grade)