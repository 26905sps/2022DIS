file = open('text files/panagram.txt')
contents = file.readlines()
setword = set(list('abcdefghijklmnopqrstuvwxyz'))
for line in contents:
    f = set('')
    line = line.strip('\n')
    for x in line.lower():
        if x in setword:
            f.add(x.lower())
    missing = setword.difference(f)
    print(line)
    if len(missing) == 0:
        print('    ','Panagram')
    else:
        list_of_strings = [str(s) for s in missing]
        stringj =''.join((sorted(list_of_strings)))
        print('    ','not panagram missing:',stringj)