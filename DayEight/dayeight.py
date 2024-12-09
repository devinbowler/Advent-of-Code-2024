import math
from math import sqrt
import copy
# Advent of Code Day #8 | Part #1
cityMap = []
antinodes = 0

with open("data.txt", "r") as city:
    for strip in city:
        stripLine = []
        for block in strip.strip():
            if block == '.':
                stripLine.append('.')
            else:
                stripLine.append(block)

        cityMap.append(stripLine)


nodeMap = copy.deepcopy(cityMap)


def findAntinode(city, aType, x, y):
    global nodeMap
    # Find all antinodes at current node, and change citymap
    for line_index, line in enumerate(cityMap):
        for block_index, block in enumerate(line):
            if (line_index is not y and block_index is not x and block == aType):
                xDelta = block_index - x 
                yDelta = line_index - y
                newNodeX = block_index + xDelta
                newNodeY = line_index + yDelta

                while 0 <= newNodeY < len(city) and 0 <= newNodeX < len(line):
                    city[newNodeY][newNodeX] = '#'
                    newNodeX += xDelta
                    newNodeY += yDelta

    return city



for line_index, line in enumerate(cityMap):
    for block_index, block in enumerate(line):
        if block != '.':
            nodeMap = findAntinode(nodeMap, block, block_index, line_index)

for line in nodeMap:
    print(line)
    for block in line:
        if block != '.':
            antinodes += 1


print("Unique Antinodes: ", antinodes)
