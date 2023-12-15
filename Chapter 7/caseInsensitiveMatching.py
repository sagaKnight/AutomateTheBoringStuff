# Write your code here :-)
import re

robocop = re.compile(r'robocop', re.I)
match1 = robocop.search('RoboCop is part man, part machine, all cop.')
print(match1.group())
