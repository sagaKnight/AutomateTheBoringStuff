# Write your code here :-)
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)?
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''', re.VERBOSE)

match0 = phoneRegex.search('fsdfsdf 0424830805 blah blah blah')
print(match0.group())
