# Write your code here :-)
import re

regexObject = re.compile(r'duck')
m0 = regexObject.search('The hunter finds the duck')
print(m0.group())

regexObject = re.compile(r'(duck) (and)')
m0 = regexObject.search('The hunter finds the duck and does a backflip')
print(m0.group(2))


regexObject = re.compile(r'(duck)|(frog)')
m0 = regexObject.search('The hunter finds the frog')
print(m0.group())

regexObject = re.compile(r'(hu)?man')
m0 = regexObject.search('The man does a backflip')
print(m0.group())

regexObject = re.compile(r'(hu)*man')
m0 = regexObject.search('The human does a backflip')
print(m0.group())

regexObject = re.compile(r'(hu){3,5}man')
m0 = regexObject.search('The huhuhuman does a backflip')
print(m0.group())

regexObject = re.compile(r'duck|frog')
m0 = regexObject.findall('The hunter finds the frog and the duck')
print(m0)

regexObject = re.compile(r'[aeiou]')
m0 = regexObject.findall('The hunter finds the frog')
print(m0)

regexObject = re.compile(r'\d$')
m0 = regexObject.search('1 year old. 4')
print(m0.group())

regexObject = re.compile(r'Age: (.*) YOB: (.*)')
m0 = regexObject.search('Age: (15) YOB: (2000)')
print(m0.group())

regexObject = re.compile(r'Age: (.*) YOB: (.*)', re.DOTALL) # Got this wrong
m0 = regexObject.search('Age: (15) YOB: (2000)')
print(m0.group())


