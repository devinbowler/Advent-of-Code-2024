# Advent of Code Day #11
from functools import lru_cache
class Node:
    """A node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A simple implementation of a linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append an item to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self):
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        """Return a string representation of the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

def partOne():
    rockLine = []
    with open("data.txt", "r") as file:
        for line in file:
            for rock in line.strip().split(" "):
                rockLine.append(int(rock))

    
    def applyRule(line, index):
        if(line[index] == 0):
            line[index] = 1
        elif(len(str(line[index])) % 2 == 0):
            num_str = str(line[index])
            mid_index = len(num_str) // 2
            first_half = int(num_str[:mid_index])      
            second_half = int(num_str[mid_index:])

            if second_half == 0:
                second_half = 0
            line[index] = first_half
            line.insert(index + 1, second_half)
            index += 1

        else:
            line[index] = line[index] * 2024

        return [line, index + 1]
        
    newLine = rockLine

    for _ in range(25):
        index = 0
        while index < len(newLine):
            result = applyRule(newLine, index)
            newLine = result[0]
            index = result[1]
            
            
    print(newLine)


def partTwo():
    # Initialize the linked list from data.txt
    stoneInput = LinkedList()
    with open("data.txt", "r") as file:
        for line in file:
            for rock in line.strip().split(" "):
                stoneInput.append(int(rock))

    @lru_cache(maxsize=None)
    def count_stones(stones, blinks):
        if blinks == 0:
            return 1

        str_stones = str(stones)
        if stones == 0:
            return count_stones(1, blinks-1)
        elif len(str_stones) % 2 == 0:
            mid = len(str_stones) // 2
            left = int(str_stones[:mid])
            right = int(str_stones[mid:])
            return count_stones(left, blinks-1) + count_stones(right, blinks-1)
        else:
            return count_stones(stones * 2024, blinks-1)

    # Start counting the stones for each initial value
    finalResult = 0  # Correct initialization of final result
    node = stoneInput.head
    while node:
        finalResult += count_stones(node.data, 75)
        node = node.next

    print(f"Final result: {finalResult}")



# partOne()
partTwo()
