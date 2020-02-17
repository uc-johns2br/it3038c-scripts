#Script to count letters, vowels, and consonants in a word.

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



#Count vowels and consonants
length = len(word)

for l in range (0, length):
    if word[l] in consonants:
        numOfConsonants += 1
    else:
        numOfVowels += 1
##endloop

#Print output
print ("%s has %s letters; %s consonants and %s vowels."% (word, length, numOfConsonants, numOfVowels))
