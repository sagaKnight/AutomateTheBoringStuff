# Write your code here :-)
import re

phoneNumRegex = re.compile(r'(04\d\d)-(\d\d\d)-(\d\d\d)')
match = phoneNumRegex.search('My Victorian number is 0424-810-820.')
areaCode, midNumber, endNumber = match.groups()
print(match.groups())
print(areaCode)
