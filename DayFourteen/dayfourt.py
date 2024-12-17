# Advent of Code Day 14
import re
import copy
import time

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
        for line in hqRoom:
            print(line)


        

    print("Q1 Count: ", countQ1) 
    print("Q2 Count: ", countQ2) 
    print("Q3 Count: ", countQ3) 
    print("Q4 Count: ", countQ4)
    result = countQ1 * countQ2 * countQ3 * countQ4
    print("Final Safety Factor: ", result)



def partTwo():
    # Parse the input from the file
    with open('data.txt', 'r') as f:
        r_inp = f.read()

    robots = []

    # Parse each line of the input
    for l in r_inp.strip().split("\n"):
        if not l: 
            continue
        # Extract position and velocity
        problem = []
        eq_split = l.split("=")
    
        p_split = eq_split[1].split(",")
        problem.append(int(p_split[0].strip()))
        problem.append(int(p_split[1].split(" ")[0].strip()))
    
        v_split = eq_split[2].split(",")
        problem.append(int(v_split[0].strip()))
        problem.append(int(v_split[1].strip()))
    
        robots.append(tuple(problem))

    # Loop through the range of t seconds (this could be up to 10,000)
    for t in range(10000):
        # Step 1: Find robots close to each other
        next_set = set()
        matching = set()
    
        for px, py, vx, vy in robots:
            # Calculate position after `t` seconds with wrapping
            xf, yf = (px + t * vx) % 101, (py + t * vy) % 103
        
            # If this position is already in the set, add it to matching
            if (xf, yf) in next_set:
                matching.add((xf, yf))
        
            # Add all neighboring positions to the set (3x3 grid around it)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    next_set.add((xf + dx, yf + dy))
    
        # Step 2: Print the board if there are enough matching robots
        if len(matching) > 250:
            print(f"\nTime = {t} seconds - Robots in a cluster: {len(matching)}\n")
        
            # Print the 2D grid (up to a 100x100 area)
            for y in range(50):  # Print first 50 rows only for visibility
                for x in range(101):  # Print all 101 columns
                    if (x, y) in matching:
                        print("*", end="")
                    else:
                        print(".", end="")
                print("")
        
            print(f"t: {t}")
            break  # Exit after printing the grid (remove this if you want it to run until 10,000)


partTwo()
# partOne()
