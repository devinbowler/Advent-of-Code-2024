# Advent of Code Day #9
spaceArray = []
isSpace = False
count = 0

# Read the input (a single very long line) and convert it into blocks
# Even indices -> file block counts, Odd indices -> free space counts
with open("data.txt", "r") as file:
    for line in file:
        for num in line.strip():
            if isSpace:
                # Add '.' for free spaces
                for _ in range(int(num)):
                    spaceArray.append('.')
                isSpace = False
            else:
                # Add block IDs for files
                for _ in range(int(num)):
                    spaceArray.append(count)
                count += 1
                isSpace = True

# The approach:
# 1. Identify the rightmost block.
# 2. Try to place it into the earliest large enough free space on the left.
# 3. If placed, remove it from the right and insert it on the left.
# 4. If no suitable free space is found, leave the block in place and move on.
# 5. Repeat until no changes occur.

while True:
    moved = False
    # We'll scan from the right to left for blocks
    left = 0
    right = len(spaceArray) - 1

    # Move through all blocks from right to left in one full pass
    while left < right:
        # Find the rightmost block (skip trailing '.')
        while right > left and right >= 0 and spaceArray[right] == '.':
            right -= 1
        if left >= right:
            # No more blocks to move
            break

        currentValue = spaceArray[right]
        # Determine the size of this block
        sizeOfBlock = 0
        blockEnd = right
        while blockEnd >= 0 and spaceArray[blockEnd] == currentValue:
            sizeOfBlock += 1
            blockEnd -= 1

        # Attempt to place the block in a suitable free space
        blockPlaced = False
        # Start scanning free spaces from the very beginning each time
        freeScan = 0
        while freeScan < right and not blockPlaced:
            if spaceArray[freeScan] == '.':
                # Measure size of this free space run
                sizeOfSpace = 0
                freeScanDummy = freeScan
                while freeScanDummy < len(spaceArray) and spaceArray[freeScanDummy] == '.':
                    sizeOfSpace += 1
                    freeScanDummy += 1

                if sizeOfSpace >= sizeOfBlock:
                    # The block fits here
                    # Remove the block from the right side
                    for i in range(sizeOfBlock):
                        spaceArray[right - i] = '.'
                    # Place the block on the left side free space
                    for i in range(sizeOfBlock):
                        spaceArray[freeScan + i] = currentValue

                    # Update pointers: The block is now placed
                    # Move right pointer to the end of the previous block
                    right = blockEnd
                    moved = True
                    blockPlaced = True
                else:
                    # Doesn't fit, skip this space run
                    freeScan = freeScanDummy
            else:
                freeScan += 1

        if not blockPlaced:
            # Couldn't place the block anywhere, leave it where it is.
            # Move on to the next block to the left
            right = blockEnd

    # If in this full pass we haven't moved any block, we are done
    if not moved:
        break

# Compute the checksum
checkSum = 0
for index, num in enumerate(spaceArray):
    if num != '.':
        checkSum += int(num) * index

print(spaceArray)
print(checkSum)

