""" In this script we will try to create a game of hangman"""

TECHMODAL_MISSION_STATEMENT = """
The mission of Techmodal is to maintain its outstanding
reputation in delivering high quality tools that are key 
enablers in our customers operational and strategic
decisions Continuing to employ and develop high calibre
individuals that are capable of delivering a quality
service to our customers
"""


word_list = TECHMODAL_MISSION_STATEMENT.split()
word_list = [x.lower() for x in word_list if len(x) >= 4] # filter for words with 4 letters or more

print(word_list)
print()

word = 'test'
guessed_letter = input('Enter your guess:')
if guessed_letter in word:
    print("yes, " + guessed_letter + "is in the word")