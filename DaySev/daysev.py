# Advent of Code Day 7, Part #1
calibrations = []
validTest = []
returnSum = 0

with open("data.txt", "r") as file:
    for line in file:
        appendList = []
        for num in line.strip().split(" "):
            appendList.append(int(num.rstrip(":")))

        calibrations.append(appendList)



def calc(values, target, index=1, current_result=None):
    # Base case: if we've hit the target exactly
    if current_result is None:
        current_result = values[0]
    
    if index == len(values):
        return current_result == target
    
    # Recursive step:
    if calc(values, target, index + 1, current_result + values[index]):
        return True

    if calc(values, target, index + 1, current_result * values[index]):
        return True

    if calc(values, target, index + 1, int(str(current_result) + str(values[index]))):
        return True

    return False


    
for calibration in calibrations:
    result = calibration[0]
    values = calibration[1:]

    if calc(values, result):
        print(result)
        validTest.append(result)
    else:
        pass


for value in validTest:
    returnSum += value
print(returnSum)
