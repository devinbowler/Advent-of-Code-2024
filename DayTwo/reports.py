# Open the file and save each line
eachLine = []

with open("data.txt", "r") as file:
    for line in file:
        lineAdd = line.strip('\n')
        eachLine.append(lineAdd)

safeCount = 0

def is_valid(nums):
    isInc = None  # Start with no direction determined
    valid = True  # Assume the sequence is valid until proven otherwise

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]

        # Check for equal numbers (invalid)
        if diff == 0:
            valid = False
            return False

        # Check if the difference is outside the allowed range
        if abs(diff) > 3:
            valid = False
            return False

        # Determine direction if not set
        if isInc is None:
            isInc = diff > 0  # True for increasing, False for decreasing

        # Check for consistent direction
        elif (isInc and diff < 0) or (not isInc and diff > 0):
            valid = False
            return False

    return valid

for line in eachLine:
    nums = [int(num) for num in line.strip().split(' ')]
    print(nums)

    if is_valid(nums):
        print(f"Valid sequence: {nums}")
        safeCount += 1
    else:
        # Try removing one level at each position
        found_valid = False
        for i in range(len(nums)):
            nums_modified = nums[:i] + nums[i+1:]
            if is_valid(nums_modified):
                print(f"Valid sequence after removing nums[{i}] = {nums[i]}: {nums_modified}")
                safeCount += 1
                found_valid = True
                break
        if not found_valid:
            print(f"No valid sequence found for {nums}")

print(f"Safe count: {safeCount}")

