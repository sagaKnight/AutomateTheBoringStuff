# Write your code here :-)
# Conway's Game of Life
import random, time, copy
width = 60
height = 20

# Create a list of list for the cells:
nextCells = []
for x in range(width):
    column = [] # Create a new column.
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nexCells.append(column) #nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Seperate each step with new lines.
    currentCells = copy.deepcopy(nextCells)

for y in range(height):
    for x in range(width):

