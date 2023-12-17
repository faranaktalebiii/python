Count = 0
SUMScore = 0
while True:
    Score = input ("Please Enter Student's Score:")
    if Score == "exit":
        break
    else:
        Score = float (Score)
        SUMScore = SUMScore + Score
        print (SUMScore)
        Count = Count + 1
        GPA = SUMScore / Count
print ("Number of Lessons:", Count)
print ("Sum of Lesson's Score:" ,SUMScore)
print ("The GPA Is:",GPA)
