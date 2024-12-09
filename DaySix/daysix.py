# AoC Day #6 | Part 1

# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

roomMap = []
stepsTaken = set()
x, y = 0, 0
direction = 'N'  # Will set after we find the guard

with open("data.txt", "r") as room:
    for line_index, path in enumerate(room):
        pathLine = []
        for step_index, step in enumerate(path.strip()):
            if step == '.':
                pathLine.append(1)
            elif step == '#':
                pathLine.append(2)
            else:
                # Guard starting position
                pathLine.append(1)
                y = line_index
                x = step_index
                # Guard always starts facing north, so direction = 'N'
                # We don't need to check the symbol since you've stated always north.
                direction = 'N'
        roomMap.append(pathLine)

# For loop detection
visited_states = set()
loop_detected = False

def check_loop(x, y, direction):
    global loop_detected
    state = (x, y, direction)
    if state in visited_states:
        loop_detected = True
    visited_states.add(state)

def walkNorth(room, cx, cy):
    global direction
    direction = 'N'
    while cy - 1 >= 0 and room[cy - 1][cx]:
        if cy - 1 < 0:
            return
        if (room[cy - 1][cx] == 2):
            walkEast(room, cx, cy)
            break
        cy -= 1
        stepsTaken.add((cx, cy))
        check_loop(cx, cy, direction)
        if loop_detected:
            return

def walkSouth(room, cx, cy):
    global direction
    direction = 'S'
    while cy + 1 < len(room) and room[cy + 1][cx]:
        if cy + 1 >= len(room):
            return
        if (room[cy + 1][cx] == 2):
            walkWest(room, cx, cy)
            break
        cy += 1
        stepsTaken.add((cx, cy))
        check_loop(cx, cy, direction)
        if loop_detected:
            return

def walkEast(room, cx, cy):
    global direction
    direction = 'E'
    while cx + 1 < len(room[cy]) and room[cy][cx + 1]:
        if cx + 1 >= len(room[cy]):
            return
        if (room[cy][cx + 1] == 2):
            walkSouth(room, cx, cy)
            break
        cx += 1
        stepsTaken.add((cx, cy))
        check_loop(cx, cy, direction)
        if loop_detected:
            return

def walkWest(room, cx, cy):
    global direction
    direction = 'W'
    while cx - 1 >= 0 and room[cy][cx - 1]:
        if cx - 1 < 0:
            return
        if (room[cy][cx - 1] == 2):
            walkNorth(room, cx, cy)
            break
        cx -= 1
        stepsTaken.add((cx, cy))
        check_loop(cx, cy, direction)
        if loop_detected:
            return

# Function to simulate from the start with the current map configuration
def simulate():
    global visited_states, loop_detected, direction
    visited_states.clear()
    loop_detected = False
    stepsTaken.clear()
    direction = 'N'  # guard always starts facing north
    check_loop(x, y, direction)  # starting state
    walkNorth(roomMap, x, y)
    return loop_detected

loop_positions = []
original_map = [row[:] for row in roomMap]

for line_idx in range(len(roomMap)):
    for step_idx in range(len(roomMap[line_idx])):
        if (line_idx == y and step_idx == x):
            # Guard's start position - skip
            continue
        if roomMap[line_idx][step_idx] == 1:
            # Place obstacle
            roomMap[line_idx][step_idx] = 2
            if simulate():
                # If loop detected, record position
                loop_positions.append((step_idx, line_idx))
            # Revert the cell
            roomMap[line_idx][step_idx] = 1

print("Number of loop-causing positions:", len(loop_positions))
print("Positions:", loop_positions)

