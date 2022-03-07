import random
rolls = int(input('enter rolls'))
under = 0
craps = 0
over = 0

for i in range(rolls):
    num1= random.randint(1, 6)
    num2= random.randint(1, 6)
    print(num1, num2)
    if num1 + num2 == 7:
        craps += 1
    if num1 + num2 > 7:
        under += 1
    if num1 + num2 < 7:
        over += 1

print('under', under)
print('over', over)
print('craps', craps)