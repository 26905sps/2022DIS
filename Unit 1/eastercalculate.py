year = int(input('enter year'))
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = ((2*b) + (4*c) + (6*d) + 5) % 7
date = 22 + d + e


if year < 1982 or year > 2048:
    print('invalid year')

elif date < 31:
    print ('march', date)
else:
    print ('april', date - 31)
