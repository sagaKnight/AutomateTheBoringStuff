# Write your code here :-)
import pyinputplus as pyip

response = pyip.inputNum('Enter a roman numeral \n', allowRegexes=[r'X|V|I'])
print(response)

response = pyip.inputNum('Enter a roman numeral \n', blockRegexes=[r'2|4|6|8$'])
