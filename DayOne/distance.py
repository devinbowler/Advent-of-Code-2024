# Sort both sides of the list.
# listOne = []
# listTwo = []
# listDistance = []
#
# with open("data.txt", "r") as file:
#    for line in file:
#        numbers = line.strip().split("   ")
#        listOne.append(numbers[0])
#        listTwo.append(numbers[1])
#
#leftList = sorted(listOne)
#rightList = sorted(listTwo)
#distanceList = []
#
#for i in range(len(leftList)):
#    try:
#        distance = abs(int(rightList[i]) - int(leftList[i]))
#        distanceList.append(distance)
#    except ValueError:
#        print(f"Invalid entry at index {i}: '{leftList[i]}', '{rightLis#t[i]}'")
#
#
#print(sum(distanceList))

leftList = []
rightList = []
totalScores = []

with open("data.txt", "r") as file:
    for line in file:
        numbers = line.strip().split("   ")
        leftList.append(numbers[0])
        rightList.append(numbers[1])

for valueL in leftList:
    count = 0
    for valueR in rightList:
        if(int(valueL) == int(valueR)):
            count += 1
        else:
            continue

    score = int(valueL) * count
    if(score != 0):
        totalScores.append(score)
    

print(totalScores)
print("Length of list: ", len(totalScores))
print(sum(totalScores))
