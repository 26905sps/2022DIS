file = open('text files/selfdivi.txt')
contents = file.readlines()
for line in contents:
    line = line.strip('\n')
    values = line.split()
    start = int(values[0])
    end = int(values[1]) + 1
    count = 0
    for i in range(start, end):
        x = str(i)
        valid = True

        if '0' not in x:
            if len(x) > 0:
                for j in range(len(x)):
                    if int(x[: j+1]) % int(x[j]) != 0:
                        valid = False

        else:
            valid = False

        if valid == True:
            count += 1

    print('number of self divisible numbers between', start, 'and', end - 1,'is', count)