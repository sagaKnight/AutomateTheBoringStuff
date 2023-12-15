# Write your code here :-)
import re

haRegex = re.compile(r'(Ha){1,3}')
match1 = haRegex.search('HaHaHa')
print(match1.group())
