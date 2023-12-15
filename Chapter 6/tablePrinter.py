# Write your code here :-)
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'Bart'],
            ['dogs', 'cats', 'moose', 'goose']]

# This function needs to be able to print a nested list.
# It also needs to turn it into a table with each column being right-justified.
def printTable(tableData):

    # Empty list that creates 3, 0 values in the list.
    colWidths = [0] * len(tableData)
    colIndex = 0

    #Uses colIndex to += 1 to get to the next list. ITERATE WORTHY
    for list in tableData:
        for item in list:
            if len(item) > colWidths[colIndex]:
                colWidths[colIndex] = len(item)
        colIndex += 1

    for i, col in enumerate(colWidths):
        # Using enumerate(), if i is greater than the highest value. -
        # Change the first index colWidths to the highest value.
        if colWidths[i] > colWidths[0]:
            colWidths[0] = colWidths[i]

    for lists in range(len(tableData[0])):
        for item in range(len(tableData)):
            print(tableData[item][lists].rjust(colWidths[item]), end = ' ')
        print()
        item += 1

printTable(tableData)

'''
Used a resource to figure out the solution from StackOverflow.
I got stuck on the column printing. I didn't know about how to use 2D lists.
'''
