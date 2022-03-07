import random
money = int(input('enter money'))
rolls = 0
max = money

while money > 0:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    s = d1 + d2
    print('d1',d1,'d2',d2)

    if s == 7:
        money += 4
        rolls += 1

    elif money != 0:
        money = money - 1
        rolls += 1

    if max < money:
        max = money

    print('$',money)
print('rolls',rolls, 'maximum pot',max)


