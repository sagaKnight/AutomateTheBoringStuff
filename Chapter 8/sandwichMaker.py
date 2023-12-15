# Write your code here :-)
import pyinputplus as pyip

print('Welcome to Sandwich Haven, what would you like on your sandwich?')
bread = pyip.inputMenu(prompt='What type of bread would you like? \n', choices=['Wheat', 'White', 'Sourdough'])
protein = pyip.inputMenu(prompt='What type of protein would you like? \n', choices=['Chicken', 'Turkey', 'Ham', 'Tofu'])
cheeseBool = pyip.inputYesNo('Would you like cheese? \n')
cheeseType = 'none'
if cheeseBool == 'yes':
    cheeseType = pyip.inputMenu(prompt='What type of cheese would you like? \n', choices=['Cheddar', 'Swiss', 'Mozzarella'])
mayo = pyip.inputYesNo('Would you like mayo? \n')
mustard = pyip.inputYesNo('Would you like mustard? \n')
lettuce = pyip.inputYesNo('Would you like lettuce? \n')
tomato = pyip.inputYesNo('Would you like tomato? \n')
totalNum = pyip.inputInt('How many sandwiches do you want? \n',min=1)

def priceCalculation(bread, protein, cheeseType, cheeseBool, mayo, mustard, lettuce, tomato, totalNum):
    totalPrice = 0

    if bread == 'Wheat':
        totalPrice += 1.87
    elif bread == 'White':
        totalPrice += 1.90
    else:
        totalPrice += 1.95

    if protein == 'Chicken':
        totalPrice += 6.10
    elif protein == 'Turkey':
        totalPrice += 3.72
    elif protein == 'Ham':
        totalPrice += 4.27
    elif protein == 'Tofu':
        totalPrice += 3.48

    if cheeseBool == 'yes':
        if cheeseType == 'Cheddar':
            totalPrice += 1.73
        elif cheeseType == 'Swiss':
            totalPrice += 1.34
        elif cheeseType == 'Mozzarella':
            totalPrice += 1.84

    if mayo == 'yes':
        totalPrice += 0.74

    if mustard == 'yes':
        totalPrice += 0.74

    if lettuce == 'yes':
        totalPrice += 0.73

    if tomato == 'yes':
        totalPrice += 0.87

    if totalNum > 1:
        totalPrice = totalNum * totalPrice

    print(totalPrice)

priceCalculation(bread, protein, cheeseType, cheeseBool, mayo, mustard, lettuce, tomato, totalNum)
