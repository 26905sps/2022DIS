import random
num = int(input('enter number'))
f = 0
for i in range(2, num + 1):
    if num % i == 0:
        print (i)
        f += 1

if f > 1:
    print(num, 'not prime')
else:
    print(num, 'is prime')

