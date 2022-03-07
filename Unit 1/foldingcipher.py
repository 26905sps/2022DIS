file = open('text files/messagencrpyt.txt')
message = 'II REOA LAI NYWLRVMD'
key = ((ord(message[0]) - 64) % 3) + 3
rows = len(message) // 3

if len(message) % 3 > 0:
    rows += 1

clean_msg = ('')

for j in range(0, rows):
    clean_msg += message(j)

    for i in range(i, key):
        clean_msg += message(j + (rows*i))

print(clean_msg)