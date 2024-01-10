list = [7,2,14,7,7,6,3,2]
purelist= []
for i in range(len(list)):
    if list[i] not in purelist:
        purelist.append(list[i])
    
print(purelist)