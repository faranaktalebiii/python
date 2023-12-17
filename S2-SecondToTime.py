while True:
    UserInput = int(input ("Please Enter Your Second: "))
    Hour = int(UserInput / 3600)
    Minute = int(((UserInput / 3600) - Hour) * 60)
    Second = round((((UserInput / 3600) - Hour) * 60 - Minute) * 60)

    print (Hour,":", Minute,":", Second)