# for every number between 1 and 100 either print number
# if its multiple of 3 print fizz
# if multiple 5 print buzz if multiple of 3 and 5 print fizzbuzz

for x in range (0, 101):
    msg = ''
    if x % 3 == 0:
        msg += 'fizz'
    if x % 5 == 0:
        msg += 'buzz'
    if msg == '':
        msg = x
    print(msg)