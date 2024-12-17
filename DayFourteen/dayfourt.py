# Advent of Code Day 14
import re
import copy

def partOne():
    robotPaths = []
    hqRoom = [['.'] * 101 for _ in range(103)]
    pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                subarray = [int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))]
                robotPaths.append(subarray)


    countQ1, countQ2, countQ3, countQ4 = 0, 0, 0, 0

    for line in robotPaths:
        xCord = line[0]
        yCord = line[1]
        newX = xCord
        newY = yCord
        hqRoom[yCord][xCord] = 1
        for _ in range(100):
            print(xCord, yCord)
            print(newX, newY)
            newX = (newX + line[2]) % 101
            newY = (newY + line[3]) % 103
            hqRoom[yCord][xCord] = '.'

            xCord = newX
            yCord = newY
            

            hqRoom[newY][newX] = 1


            if _ == 99:    
                if yCord < 51 and xCord < 50:
                    countQ1 += 1
                elif yCord < 51 and xCord > 50:
                    countQ2 += 1 
                elif yCord > 51 and xCord < 50:
                    countQ3 += 1 
                elif yCord > 51 and xCord > 50:
                    countQ4 += 1 
                else: 
                    pass


        

    print("Q1 Count: ", countQ1) 
    print("Q2 Count: ", countQ2) 
    print("Q3 Count: ", countQ3) 
    print("Q4 Count: ", countQ4)
    result = countQ1 * countQ2 * countQ3 * countQ4
    print("Final Safety Factor: ", result)







def partTwo():
    pass

partOne()
