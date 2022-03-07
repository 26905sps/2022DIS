aa = int(input('What to convert 1, 2 or 3'))

#temperature converter
if aa == 1:
    tempc = float(input('Enter temperature in C'))
    tempf = (tempc * (9/5) + 32)
    print('Fahrenehit',tempf)

#distance convert
if aa == 2:
    mile = float(input('enter speed in miles'))
    km = (mile * 1.609)
    print('km', km)

if aa == 3:
#moon weight
    we = float(input('earth weight in kg'))
    wm = (we * 0.165)
    print('moon weight', wm)
