# Write your code here :-)
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook is not looking good',
    'Very doubtful']

#Print messages' list with random.random integer function(where first number is 0, and ends with the length of the messages list - 1)
print(messages[random.randint(0, len(messages) - 1)])
