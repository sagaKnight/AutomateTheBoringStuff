# Write your code here :-)
import re

phoneNumRegex = re.compile(r'04\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 042-555-4242.')
print('Phone number found: ' + mo.group())
