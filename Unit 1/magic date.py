date = (input('enter date in dd/mm/yy'))
year = int(date[6:])
month = int(date[3:4])
day = int(date[0:1])
magic = False
if day * month == year:
    print(year)
else:
    print()
