# Advent of Code Day #9

def parse_disk(line: str):
    # Parse the input line into a disk array
    # Alternating runs: file-length, space-length, file-length, space-length, ...
    disk = []
    is_space = False
    file_id = 0
    i = 0
    while i < len(line):
        length = int(line[i])
        i += 1
        if length > 0:
            if is_space:
                # Append free spaces
                disk.extend(['.'] * length)
                is_space = False
            else:
                # Append file blocks with current file_id
                disk.extend([str(file_id)] * length)
                file_id += 1
                is_space = True
        else:
            # A run of length zero means skip? Problem states runs alternate,
            # a '0' means a run of size zero. We just flip space/file?
            # According to problem: a digit 0 means run length zero of that type.
            # Just flip is_space and continue
            is_space = not is_space

    return disk, file_id - 1  # file_id - 1 is the highest file id assigned

def find_file(disk, fid):
    # Find the continuous run of file blocks with ID=fid (as string)
    fid_str = str(fid)
    start = None
    end = None
    for idx, val in enumerate(disk):
        if val == fid_str:
            if start is None:
                start = idx
            end = idx
    return start, end

def find_free_space(disk, required_length, limit_index):
    # Find a leftmost free space run to the LEFT of limit_index that can hold required_length
    # limit_index is the start of the file, we look for space runs strictly before it
    best_start = None
    i = 0
    while i < limit_index:
        if disk[i] == '.':
            run_start = i
            # Measure free space run
            while i < limit_index and i < len(disk) and disk[i] == '.':
                i += 1
            run_length = i - run_start
            if run_length >= required_length:
                # Return immediately the first suitable free space
                return run_start
        else:
            i += 1
    return best_start

def move_file(disk, file_id):
    # Move the file with ID=file_id according to the rules
    start, end = find_file(disk, file_id)
    if start is None:
        # File not found (maybe zero-length?), do nothing
        return
    file_length = (end - start + 1)

    # Find a suitable free space to the left
    free_start = find_free_space(disk, file_length, start)
    if free_start is not None:
        # Move the file there
        fid_str = str(file_id)
        # Clear old position
        for i in range(start, end+1):
            disk[i] = '.'
        # Place file in free space
        for i in range(file_length):
            disk[free_start + i] = fid_str

def compute_checksum(disk):
    checksum = 0
    for i, val in enumerate(disk):
        if val != '.':
            checksum += int(val)*i
    return checksum


# ---------------------
# Main execution logic
# ---------------------

# If your input is in a file named "data.txt", use the code below.
# Otherwise, you can store the huge line in a variable `input_data` and pass it directly.

with open("data.txt", "r") as f:
    input_data = f.read().strip()

disk, max_file_id = parse_disk(input_data)

# Move each file once in order of decreasing file ID number
for fid in range(max_file_id, -1, -1):
    move_file(disk, fid)

cs = compute_checksum(disk)
print(cs)

