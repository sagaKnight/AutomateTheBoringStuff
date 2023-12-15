# Write your code here :-)
import re

optionalRegex = re.compile(r'bat(wo)*man')
match = optionalRegex.search('The adventures of batwowowowowowowowowowoman')
print(match.group())

match = optionalRegex.search('The adventures of batman')
print(match.group())
