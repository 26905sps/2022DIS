file = open('text files/results.txt')
contents = file.readlines()
marks = ''
names = ''
for line in contents:
    line = line.strip('\n')
    if line.isdigit():
        marks += line + ' '
    else:
        names += line + ' '
    n1 = names.split()
    m1 = marks.split()
    for i in range(m1):
        name = n1[i]
        mark = m1[i]
        print(name,mark)
print(n1)

