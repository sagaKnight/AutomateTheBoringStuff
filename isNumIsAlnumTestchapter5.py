# Write your code here :-)
while True:
    print('Enter your age:')
    ageInput = input()
    if ageInput.isdecimal() == True:
        break
    else:
        print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only)')
    passwordInput = input()
    if passwordInput.isalnum() == True:
        break
