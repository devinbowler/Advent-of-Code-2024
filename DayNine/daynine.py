# Advent of Code Day #9
spaceArray = []
isSpace = False
count = 0

# Taking the input and formatting it into free space and block size (input 12345 becomes 0..111....22222)
with open("data.txt", "r") as file:
    for line in file:
        for num in line.strip():
            if isSpace:
                for index in range(int(num)):
                    spaceArray.append('.')
                isSpace = False
            else:
                for index in range(int(num)):
                    spaceArray.append(count)
                count += 1
                isSpace = True

# count is now the total number of files (highest file ID = count - 1)

def find_file(disk, fid):
    """Find the start and end index of the file with ID fid in the disk."""
    start = None
    end = None
    for i, val in enumerate(disk):
        if val == fid:
            if start is None:
                start = i
            end = i
    return start, end

def find_free_space(disk, length_needed, limit_index):
    """
    Find the leftmost free space run to the LEFT of limit_index
    that can hold length_needed blocks.
    limit_index is the start of the file's current position.
    """
    i = 0
    while i < limit_index:
        if disk[i] == '.':
            run_start = i
            # measure the free run
            while i < limit_index and i < len(disk) and disk[i] == '.':
                i += 1
            run_length = i - run_start
            if run_length >= length_needed:
                return run_start
        else:
            i += 1
    return None

# Move each file exactly once, starting from the highest file ID
for fid in range(count - 1, -1, -1):
    fid_str = fid  # Our disk uses integers for file IDs
    start, end = find_file(spaceArray, fid_str)
    if start is None:
        # File not found; skip
        continue
    file_length = end - start + 1

    # Find a suitable free space to the left
    free_start = find_free_space(spaceArray, file_length, start)
    if free_start is not None:
        # Move the file
        # Clear old position
        for i in range(start, end + 1):
            spaceArray[i] = '.'
        # Place it in the new free space
        for i in range(file_length):
            spaceArray[free_start + i] = fid_str


# Compute checksum
checkSum = 0
for index, num in enumerate(spaceArray):
    if num != '.':
        result = int(num) * index
        checkSum += result

print(spaceArray)
print(checkSum)

