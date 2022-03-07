speed = int(input('enter your speed in km/h'))
fine = 0
if speed <= 100:
    print('speed is legal')
elif speed > 100:
    s = speed
    s = (s - 100) * 5
    fine = s
    if speed > 120:
        fine = fine + 200
    print('fine is $',fine)
