#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Splits the text by finding the \n and splitting().
lines = text.split('\n')

# For i, starting from 0 to the max lines
for i in range(len(lines)):
    #Checking through the indexes, add a * per line[i]
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

'''

'''
