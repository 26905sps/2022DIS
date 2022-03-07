student_ages = {}
student_ages['Elliot'] = 16
student_ages['Ronan'] = 17
student_ages['Matthew'] = 17
student_ages['Louis'] = 18
print(len(student_ages))

if 'Ronan' in student_ages:
   print(student_ages['Ronan'])

name = input('Enter name')
if name not in student_ages:
    age = int(input('enter age'))
    student_ages[name] = age

print(student_ages)

#homework
#find out how to loop through dictonary and print out key and value
for i in student_ages:
    print(i,'is', student_ages[i])