#! python3
#mclip.py - A multi-clipboard program.

TEXT = {'agree': '''Yes, I think so. That sounds fine to me.''',
        'busy': '''Sorry, can we do this later this week, or possibly the next week?''',
        'upsell': '''Would you consider changing your mind if the plan was slightly altered?'''}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

