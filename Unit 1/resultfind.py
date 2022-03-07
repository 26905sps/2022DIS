file = open('text files/results-1line.txt')
contents = file.readlines()
A = 0
B = 0
C = 0
F = 0
for line in contents:
    line = line.strip('\n')
    values = line.split(', ')
    name = values[0]
    mark = int(values[1])
    if mark >= 80:
        grade = 'A'
        A = A + 1
    elif mark >= 70:
        grade = 'B'
        B = B + 1
    elif mark >= 50:
        grade = 'C'
        C = C + 1
    else:
        grade = 'F'
        F = F + 1

    print(name, mark, grade)

print('\nA:',A,' \nB:', B,' \nC:', C,' \nF:', F)

