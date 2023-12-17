import random
while True:
    UserAction = input ("Press r or R to Roll The Dice: ")
    if UserAction == "r" or UserAction == "R":
        Dice = random.randint(1,6)
        print ("First Roll is:", Dice)
        if Dice == 6:
           Dice = random.randint(1,6)
           print ("Second Roll is:", Dice)
   