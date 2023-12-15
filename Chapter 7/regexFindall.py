# Write your code here :-)
import re

regexFindall = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = regexFindall.findall('Cellphone Number: 123-456-7890 Work Number: 111-222-3123')
print(mo1[0])

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)') # has groups
mo2 = phoneNumRegex.findall('Cell: 415-555-9999-9999 Work: 212-555-0000-9999')
print(mo2)
