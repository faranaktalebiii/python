while True:
    UserInput = int(input ("Please Enter The Number: "))
    Count = 0
    n1= 0
    n2 = 1
    if UserInput <= 0:
        print ("Please Enter Positive Integer")
    elif UserInput == 1:
        print (n1)
    else:
        while Count < UserInput:
            print (n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            Count = Count + 1
            