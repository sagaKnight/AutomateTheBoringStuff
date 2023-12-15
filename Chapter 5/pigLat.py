# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin.
fork word in message.split():
    # Seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    # When length of the word var is greater than 0 AND
    # the word[0] is not a letter or blank it will loop
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = [1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #Seperate t
