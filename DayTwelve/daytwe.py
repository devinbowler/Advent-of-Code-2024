# Advent of Code Day #12


from collections import deque, defaultdict

def partOne():
    garden = []
    totalResult = 0

    # Read the garden from the file
    with open("data.txt", "r") as file:
        for line in file:
            # Strip newline characters and split into individual blocks
            newArray = list(line.strip())
            garden.append(newArray)


    rows = len(garden)
    cols = len(garden[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    gardenMap = {}  # Maps cluster_id to {'block': block_type, 'count': count, 'different_sides': sides}
    cluster_id = 0  # Unique identifier for each cluster

    # Define directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                current_block = garden[i][j]
                cluster_id += 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                count = 0
                different_sides = 0

                while queue:
                    x, y = queue.popleft()
                    count += 1

                    # For each direction, check neighbors
                    for dr, dc in directions:
                        ni, nj = x + dr, y + dc

                        if 0 <= ni < rows and 0 <= nj < cols:
                            neighbor_block = garden[ni][nj]
                            if neighbor_block != current_block:
                                different_sides += 1
                            else:
                                if not visited[ni][nj]:
                                    visited[ni][nj] = True
                                    queue.append((ni, nj))
                        else:
                            # Out of bounds counts as different side
                            different_sides += 1

                # Store the cluster information
                gardenMap[cluster_id] = {
                    'block': current_block,
                    'count': count,
                    'different_sides': different_sides
                }

    for cluster_id, info in gardenMap.items():
        block = info['block']
        count = info['count']
        different_sides = info['different_sides']
        result = int(count) * int(different_sides)
        totalResult += result
        print(f"Cluster {cluster_id}: Block '{block}' | Count = {count} | Different Sides = {different_sides}")
        
    print("Final Total Price: ", totalResult)

    

             



def partTwo():
    pass




partOne()
