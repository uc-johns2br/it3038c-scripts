#Script to count letters, vowels, and consonants in a word.

#definitions
vowels = 'aeiouAEIOU'
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
    if word[l] in vowels:
        numOfVowels += 1
    else:
        numOfConsonants += 1
##endloop

#Print output
print ("%s has %s letters; %s consonants and %s vowels."% (word, length, numOfConsonants, numOfVowels))
