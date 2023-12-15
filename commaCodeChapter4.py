# Write your code here :-)

exampleList = ['Tiger','Horse','Snake','Pig']

def commaFunction(theList):
    # For each
    for i in range(len(theList)):
        # If we get to the last one, add an and to it. We find the last by getting the max length of the list, and minusing by 1.
        if i == len(theList) - 1:
            print('and ' + theList[i])
        else:
            #Uses the end='' which means that at the end of the print, we need to include an emptry string called ' '. Otherwise, it will always do end='\n' automatically.
            print(theList[i] + ', ', end='')

commaFunction(exampleList)
