file = open('text files/luhn.txt')
contents = file.readlines()
contents.pop(0)
for line in contents:
    count = 0
    output = ''
    total = 0
    input = line
    for i in line:
        if i.isnumeric():
            f = int(i)
            f = f * 2
            if count % 2 != 0 and count != 0:
                output = output + str(i)
                count += 1
            elif count % 2 == 0 or count == 0:
                count += 1
                if len(str(f)) != 2:
                     output = output + str(f)
                if len(str(f)) == 2:
                    f = str(f)
                    n1 = int((f[0]))
                    n2 = int((f[1]))
                    g = n1+n2
                    output += str(g)
            #print(output)
    for i in str(output):
        i = int(i)
        total = total + i
    if total % 10 == 0:
        print(line, 'VALID')
    else:
        print(line, total, 'INVALID')



