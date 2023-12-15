# Write your code here :-)
import re

namesRegex = re.compile(r'Agent (\w)\w*')
m1 = namesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(m1)

namesRegex2 = re.compile(r'Super(\w)(\w)\w*')
m2 = namesRegex2.sub(r'\1secre\2t', 'Superhero here')
print(m2)
