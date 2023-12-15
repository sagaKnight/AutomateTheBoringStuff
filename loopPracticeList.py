# Write your code here :-)
animalList = []
numInput = input('How many animals do you want in the list? \n')
count = 0

for i in range(int(numInput)):
    count += 1
    newAnimal = input('Enter in an animal for index ' + str(count) + ': ')
    animalList.append(newAnimal)

print(animalList)
