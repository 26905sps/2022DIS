file = open('task3_test_data.txt').readlines()
for line in file:
    line = line.strip('\n')
    words = line.split()
    if len(words[0]) == len(words[1]):
        isomorph = False
        l0 = []
        l1 = []
        dict_l0 = {}
        dict_l1 = {}
        for word in words[0]:
            for i in word:
                l0.append(ord(i))
        for word in words[1:]:
            for i in word:
                l1.append(ord(i))
        for i, value in enumerate(l0):
            dict_l0[value] = dict_l0.get(value, []) + [i]
        for j, value in enumerate(l1):
            dict_l1[value] = dict_l1.get(value, []) + [j]

        if sorted(dict_l0.values()) == sorted(dict_l1.values()):
            isomorph = True
        else:
            print('not isomorph')
            isomorph - False

        aa = ''
        if isomorph == True:
            m = 0
            for i in dict_l0:
                if len(dict_l0[i]) == 2:
                    a = dict_l0[i][1] - dict_l0[i][0]
                    aa += ' ' + '+' + str(a)
                    add = True
                    m = m + 1
                elif len(dict_l0[i]) == 3:
                    a = dict_l0[i][1] - dict_l0[i][0]
                    b = dict_l0[i][2] - dict_l0[i][1]
                    aa += ' ' + '+' + str(a)
                    aa += ' ' + '+' + str(b)
                    add = True
                    m = m + 1
                elif len(dict_l0[i]) == 4:
                    a = dict_l0[i][1] - dict_l0[i][0]
                    b = dict_l0[i][2] - dict_l0[i][1]
                    c = dict_l0[i][3] - dict_l0[i][2]
                    aa += ' ' + '+' + str(a)
                    aa += ' ' + '+' + str(b)
                    aa += ' ' + '+' + str(c)
                    add = True
                    m = m + 1
                else:
                    aa += ' ' + str(0)
            if add == True:
                aa += (' ' + str(0)) * m

            print(words[0], 'and', words[1], 'is isomorph with code of',aa)

    else:
        print('length different')