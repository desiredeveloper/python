from random import shuffle

words = list(input("enter a sentence to be scrambled\n").split())
scramble = []
for word in words:
    temp = list(word)
    shuffle(temp)
    scramble.append(''.join(temp))
print(' '.join(scramble))

