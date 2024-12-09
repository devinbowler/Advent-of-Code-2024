validPages = []
allPages = []
incorrectPages = []
rulesForPages = {}

spaceFlip = False
with open("data.txt", "r") as file:
    for line in file:
        if not line.strip():
            spaceFlip = True
        elif not spaceFlip:
            rules = line.strip().split("|")
            if len(rules) >= 2:
                key = int(rules[0])
                value = int(rules[1])

                if key in rulesForPages:
                    rulesForPages[key].append(value)
                else:
                    rulesForPages[key] = [value]
        else:
            allPages.append([int(num) for num in line.strip().split(",")])

# Determine which pages are already in correct order
for page in allPages:
    skip_page = False
    # Check ordering constraints for this update
    for index in range(1, len(page)):
        # For each page (except the first), check all previous pages
        for check in range(index):
            # If a rule says page[index] must come after page[check],
            # and this violates the order, mark this page as incorrect.
            if page[check] in rulesForPages.get(page[index], []):
                skip_page = True
                break
        if skip_page:
            break

    if skip_page:
        incorrectPages.append(page)
    else:
        validPages.append(page)

# Sum of the middle pages for correctly ordered updates
totalPages = 0
for page in validPages:
    midNum = page[(len(page) - 1) // 2]
    totalPages += midNum

# Now fix the incorrectly ordered pages using a topological sort
from collections import deque

def topological_sort_pages(pages, rules):
    current_pages = set(pages)
    graph = {}
    in_degree = {}

    # Initialize graph
    for p in current_pages:
        graph[p] = []
        in_degree[p] = 0

    # Build subgraph using only rules that apply to these pages
    for X, Y_list in rules.items():
        if X in current_pages:
            for Y in Y_list:
                if Y in current_pages:
                    graph[X].append(Y)
                    in_degree[Y] += 1

    # Kahn's algorithm for topological sorting
    queue = deque([node for node in current_pages if in_degree[node] == 0])
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topological_order

# Reorder each incorrect page list properly
for page in incorrectPages:
    ordered_page = topological_sort_pages(page, rulesForPages)
    page[:] = ordered_page  # Update the page with the corrected order

# Sum of middle pages of now-correctly-ordered "incorrect" updates
total = 0
for page in incorrectPages:
    midNum = page[(len(page) - 1) // 2]
    total += midNum

print(total)

