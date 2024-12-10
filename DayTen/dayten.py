# Advent of Code Day #10


def partOne():
    topMap = []
    memo = {}

    with open("data.txt", "r") as file:
        for line in file:
            tempLine = []
            for cord in line.strip():
                tempLine.append(int(cord))
            topMap.append(tempLine)


    def findReachableNines(mapT, x, y, height):
        # If we've reached a 9 (height == 10), return this position as a reachable endpoint.
        if height == 10:
            return {(x, y)}

        # Check if we already computed this state
        if (x, y, height) in memo:
            return memo[(x, y, height)]

        reachable = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= ny < len(mapT) and 0 <= nx < len(mapT[0]):
                if mapT[ny][nx] == height:
                    reachable |= findReachableNines(mapT, nx, ny, height+1)

        memo[(x, y, height)] = reachable
        return reachable



    total_score = 0
    for y, row in enumerate(topMap):
        for x, val in enumerate(row):
            if val == 0:
                # Directly get the reachable 9 positions from this starting point
                reachable_nines = findReachableNines(topMap, x, y, 1)
                total_score += len(reachable_nines)

    print("Answer for Part 1", total_score)


def partTwo():
    topMap = []

    with open("data.txt", "r") as file:
        for line in file:
            tempLine = []
            for cord in line.strip():
                tempLine.append(int(cord))
            topMap.append(tempLine)

    total = 0  # This is part of the outer scope of searchPath

    def searchPath(mapT, x, y, counter):
        nonlocal total  # Access 'total' from the outer 'partOne' scope

        # Base case: if we have reached height 9 (counter == 10), increment total and stop this path
        if counter == 10:
            total += 1
            return  # No need to explore further from here

        # Move east
        if x + 1 < len(mapT[0]) and mapT[y][x + 1] == counter:
            searchPath(mapT, x + 1, y, counter + 1)

        # Move west
        if x - 1 >= 0 and mapT[y][x - 1] == counter:
            searchPath(mapT, x - 1, y, counter + 1)
    
        # Move north
        if y - 1 >= 0 and mapT[y - 1][x] == counter:
            searchPath(mapT, x, y - 1, counter + 1)

        # Move south
        if y + 1 < len(mapT) and mapT[y + 1][x] == counter:
            searchPath(mapT, x, y + 1, counter + 1)
    
    for index_line, line in enumerate(topMap):
        for index_cord, cord in enumerate(line):
            if cord == 0:
                searchPath(topMap, index_cord, index_line, 1)
    
    print("Answer for Part 2: ", total)


partOne()
partTwo()
