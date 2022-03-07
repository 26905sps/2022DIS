year = int(input('enter year'))
leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        leap = True


print('Result for', year,'is leap:',leap,)





