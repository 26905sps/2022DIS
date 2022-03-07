weight = float(input("enter weight in Kg"))
height = float(input('enter height in meters'))
BMI = (weight / pow(height, 2))
print (BMI)
if BMI < 18.5:
    print('BMi below healthy range')

elif BMI >= 18.5 and BMI <= 24.9:
    print('BMI within healthy range')
else:
    print('BMI above healthy range')
