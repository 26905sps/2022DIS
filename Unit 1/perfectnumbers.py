n = int(input('enter the max number'))

for i in range(1, n+1):
    total = 0
    factors = ''
    for j in range (1,i):
        if i % j == 0:
            total += j
            factors += str(j) + ''
    if total == i:
        print(i, 'is a perfect number ->1 factors',factors)