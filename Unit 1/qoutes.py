import random
filename = 'text files/quotes.txt'
file = open(filename)
#print(type(file))

contents = file.readlines()
print(type(contents))
print(len(contents))

qoute = random.choice(contents).strip('\n')
print(qoute)