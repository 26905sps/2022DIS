word1 = input('enter words')
words = word1.split()
pl = ''
for word in words:
    if len(word) > 1:
        lw = word[1:] + word[0] + 'ay'
    else:
        lw = word + 'ay'
    pl = pl + lw + ' '

print(pl.upper())