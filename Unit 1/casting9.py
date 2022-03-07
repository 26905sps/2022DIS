file = open('text files/casting9.txt')
contents = file.readlines()
for line in contents:
    line = line.strip('\n')
    total = 0
    for n in line:
        total += (int(n))
        if total >= 9:
            total = total - 9
    print(total)