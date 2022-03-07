file = open('text files/plural.txt')
contents = file.readlines()
contents.pop(0)
for line in contents:
    values = line.split(' ')
    q = values[0]
    t = values[1]
    if q == 0:
        q = 'no'
    elif q == 1:
        q = 'one'
    if q == 'one':
        if t[-1] == ('s', 'x', 'z'):
            t = t + 'es'
        elif t[-2:] == ('ch', 'sh'):
            t = t + 'es'
        elif t[-1] == 'o' and t[-2] not in ('aeiouy'):
            t = t + 'es'
        elif t[-1] == 'y' and t[-2] not in ('aeiouy'):
            t = t[0:-1] + 'ies'
        elif t[-2:] == 'fe' and t[-3] != 'f':
            t = t[0:-2] + 'ves'
        elif t[-1] == 'f' and t[-2] != 'f':
            t = t[0:-1] + 'ves'
        else:
            t = t + 's'
    print(q, t)

