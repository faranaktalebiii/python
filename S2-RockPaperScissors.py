import random

    
UserScore = 0
ComputerScore = 0
##print (ComputerChoice)
while ComputerScore <3 and UserScore < 3:
    UserChoice = input("Please Enter Rock or Paper or Scissors:")
    ComputerChoice = random.randint(1,3)
    if ComputerChoice == 1:
        ComputerChoice = "Rock"
    elif ComputerChoice == 2:
        ComputerChoice = "Paper"
    else:
        ComputerChoice = "Scissors"
    print (ComputerChoice)
    
    if ComputerChoice == "Paper" and UserChoice == "Rock":
        print ("Computer won this Round")
        ComputerScore = ComputerScore + 1
        UserScore = UserScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
        ##break
    elif ComputerChoice == "Rock" and UserChoice == "Rock":
        print ("Draw!")
        ComputerScore = ComputerScore
        UserScore = UserScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break
    elif ComputerChoice == "Scissors" and UserChoice == "Rock":
        print ("You won this Round")
        UserScore = UserScore + 1
        ComputerScore = ComputerScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break
    elif ComputerChoice == "Paper" and UserChoice == "Paper":
        print ("Draw!")
        ComputerScore = ComputerScore
        UserScore = UserScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break
    elif ComputerChoice == "Rock" and UserChoice == "Paper":
        print ("You won this Round")
        UserScore = UserScore + 1
        ComputerScore = ComputerScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break
    elif ComputerChoice == "Scissors" and UserChoice == "Paper":
        print ("Computer won this Round")
        ComputerScore = ComputerScore + 1
        UserScore = UserScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break  
    elif ComputerChoice == "Paper" and UserChoice == "Scissors":
        print ("Computer won this Round")
        ComputerScore = ComputerScore + 1
        UserScore = UserScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break
    elif ComputerChoice == "Rock" and UserChoice == "Scissors":
        print ("You won this Round")
        UserScore = UserScore + 1
        ComputerScore = ComputerScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
       ## break
    elif ComputerChoice == "Scissors" and UserChoice == "Scissors":
        print ("Draw!")
        ComputerScore = ComputerScore
        UserScore = UserScore
        print ("Computer Score:", ComputerScore)
        print ("User Score:", UserScore)
      ##  break 
print ("Computer Score:", ComputerScore)
print ("User Score:", UserScore)