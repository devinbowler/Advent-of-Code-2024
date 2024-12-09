# Advent of Code Day #9
spaceArray = []
isSpace = False
count = 0

# Taking the input and formatting it into free space and
# block size (input 12345 becomes 0..111....22222)
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



# After making the input into format, make an algorithm to
# take the last digit of the string, and put it in the first
# available free spot, repeat until no freespace between nums.
left = 0
right = len(spaceArray) - 1 

while left < right:
    if spaceArray[left] == ".":
        if spaceArray[right] != ".":
            spaceArray[left] = spaceArray[right]
            spaceArray[right] = "."
        else:
            right -= 1
    else:
        left += 1

print(spaceArray)

# Return the checksum of multiplying each digit in the file
# compressed file block by its index and add them all.
checkSum = 0
for index, num in enumerate(spaceArray):
    if num != '.':
        result = int(num) * index
        checkSum += result

print(checkSum)

