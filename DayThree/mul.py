count = 0

file = open("data.txt", "r")
position = 0
doMul = True  # Start with `doMul` enabled

validMul = []
finalResults = []

while True:
    file.seek(position)
    fourChar = file.read(4)

    if not fourChar:  # EOF
        break

    # Detect and toggle `doMul`
    if fourChar == "do()":
        doMul = True
        print(f"Toggled doMul: {doMul}, position: {position}")
        position += 4  # Advance position after `do()`
        continue
    elif fourChar == "mul(" and doMul:
        number = []
        maxCount = 0

        while maxCount <= 8:
            nextChar = file.read(1)
            if not nextChar:
                break
            maxCount += 1

            if nextChar.isdigit():
                number.append(nextChar)
            elif nextChar == ',':
                number.append(nextChar)
            elif nextChar == ')':
                break
            else:
                number = []
                break

        if ',' in number:
            try:
                index = number.index(',')
                xVal = "".join(number[:index])  # Before comma
                yVal = "".join(number[index + 1:])  # After comma

                if 1 <= len(xVal) <= 3 and 1 <= len(yVal) <= 3:
                    validMul.append((xVal, yVal))
                    print(f"Valid mul: {xVal}, {yVal}")
            except:
                pass
        position += 4 + maxCount
        continue

    # Detect `don't()` for toggling `doMul`
    file.seek(position)  # Reset to current position
    sevenChar = file.read(7)
    if sevenChar == "don't()":
        doMul = False
        print(f"Toggled doMul: {doMul}, position: {position}")
        position += 7  # Advance position after `don't()`
        continue

    # Default position increment
    position += 1


# Function to calculate multiplication
def mul(X, Y):
    return abs(int(X) * int(Y))


# Process valid instructions
for each in validMul:
    xVal, yVal = each
    result = mul(xVal, yVal)
    finalResults.append(result)

print("Final result: ", sum(finalResults))

