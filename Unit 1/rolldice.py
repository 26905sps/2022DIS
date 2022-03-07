import random
d = int(input('enter number'))
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
for i in range(d):
    num = random.randint(1, 6)
    if num % 1 == 0:
        t1 +=1
    if num % 2 == 0:
        t2 += 1
    if num % 3 == 0:
        t3 += 1
    if num % 4 == 0:
        t4 += 1
    if num % 5 == 0:
        t5 += 1
    if num % 6 == 0:
        t6 += 1
    print(num)
print('1 rolled',t1)