#Script to count letters, vowels, and consonants in a word.

import re

#definitions
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
numOfVowels = int(0)
numOfConsonants = int(0)

#Ask for input
print ('Please enter a word:')
word = input()

#check for only letters
while not word.isalpha():
    print ('Letters only, please:')
    word = input()
##endloop

length = len(word)

#Count vowels and consonants
for l in length:
    if word[l] in consonants:
        numOfConsonants =+ 1
    else:
        numOfVowels =+ 1
##endloop

print ("%s has %s letters, %s consonants, and %s vowels."% (word, length, numOfConsonants, numOfVowels))
