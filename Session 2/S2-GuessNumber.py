import random
Number = random.randint(1,10)
Count = 1
print("Please guess the Number between 1 to 10")
while True:
    UserInput = int(input("Please Guess The Number: "))
    if UserInput == Number:
        print ("Yesss!, You Are Perfect.")
        print (Count)
        break
    elif UserInput > Number:
        print("Go Down Dude!")
        Count = Count + 1
    elif UserInput < Number:
        print ("Go Up Dude!")
        Count = Count + 1
        
        
