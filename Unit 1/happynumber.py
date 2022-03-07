for i in range(0, 9999):
    total = 0
    print('NUMBER', i)
    for n in str(i):
        f = int(n)
        fe = f * f
        print(fe)
        total += fe
    for i in str(total):
        count = 0
        count += 1
        total1 = total
        f = int(i)
        fe = f * f
        total = total + fe
        if count == len(str((total))):
            total = total - total1
            print(total)
