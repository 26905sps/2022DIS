file = open('text files/urldecode.txt')
contents = file.readlines()
encrypt = []
letter =  {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for line in contents:
    encrypt = ''
    i = 0
    while i < len(line):
        character = line[i]
        if character == ('%'):
            f = line(i + 1, i +3)
            print(f)
            m1 = f[0]
            m2 = f[1]
            if m1.isdigit:
                c = m1 * 16
            else:
                if m1 in letter:
                    m1 = letter[m1]
                    c = m1 * 16
            hex = c + m2
            character = ord(hex)
            i = i + 3
        else:
            i = i + 1
        encrypt += character

print(encrypt)
