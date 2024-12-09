# advent of code #4
wordsearch = []
match = ['M', 'A', 'S']
with open("data.txt", "r") as file:
    for line in file:
        newline = []
        for char in line:
            if(char != '\n'):
                newline.append(char)
        wordsearch.append(newline)

# 140(h) x 140(v) 

# horizontal
def checkh(array, x, y):
    for index in range(3):
        if(x + (index + 1) >=(len(array[y]))):
           return False
        elif(array[y][x + (index + 1)] == match[index]):
            continue
        else:
            return False

    return True

def checkbh(array, x, y):
    for index in range(3):
        if(x - (index + 1) < (0)):
           return False
        elif(array[y][x - (index + 1)] == match[index]):
            continue
        else:
            return False

    return True

# vertical
def checkv(array, x, y):
    for index in range(3):
        if(y + (index + 1) >= len(array)):
            return False
        elif(array[y + (index + 1)][x] == match[index]):
            continue
        else:
            return False
    return True

def checkbv(array, x, y):
    for index in range(3):
        if(y - (index + 1) < 0):
            return False
        elif(array[y - (index + 1)][x] == match[index]):
            continue
        else:
            return False

    return True



# diagonal
def checktld(array, x, y):
    for index in range(3):
        if((y - (index + 1) < 0) or (x - (index + 1) < 0)):
            return False
        elif(array[y - (index + 1)][x - (index + 1)] == match[index]):
            continue
        else:
            return False

    return True

def checktrd(array, x, y):
    for index in range(3):
        if((y - (index + 1) < 0) or (x + (index + 1) >= len(array[y]))):
            return False
        elif(array[y - (index + 1)][x + (index + 1)] == match[index]):
            continue
        else:
            return False

    return True

def checkbld(array, x, y):
    for index in range(3):
        if((y + (index + 1) >= len(array)) or (x - (index + 1) < 0)):
            return False
        elif(array[y + (index + 1)][x - (index + 1)] == match[index]):
            continue
        else:
            return False

    return True

def checkbrd(array, x, y):
    for index in range(3):
        if((y + (index + 1) >= len(array)) or (x + (index + 1) >= len(array[y]))):
            return False
        elif(array[y + (index + 1)][x + (index + 1)] == match[index]):
            continue
        else:
            return False

    return True

checks = [checkh, checkbh, checkv, checkbv, checktld, checktrd, checkbld, checkbrd]

xmascount = 0

def run_all_checks(array, x, y):
    global xmascount
    for check in checks:
        result = check(array, x, y)
        if result:
            xmascount += 1

#main loop
for y, line in enumerate(wordsearch):
    for x, char in enumerate(line):
        if(char == 'X'):
            run_all_checks(wordsearch, x, y)

print(xmascount)
