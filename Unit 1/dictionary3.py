#ask the user to enter a sentence or paragraph. count the number of each word in the sentance.
#example if user entered:
#The quick brown fox jumped over the lazy fox which was also brown due to the brown rain.
words = {}
sentence = input('enter sentence')
wordlist = sentence.split(' ')
print(wordlist)
for word in wordlist:
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for k, v in words.items():
    print(k, v)