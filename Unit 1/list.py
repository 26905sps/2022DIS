students = []
students.append('Peter')
students.append('Paul')
students.append('Mary')

print(type(students))
print(students)
print(students[1])
print(len(students))
print(students[-1])

for student in students:
    print(student)

students.append('Bryson')
print(students)
students.sort()
print(students)
students.reverse()
print(students)

x = students.pop()
print(x, students)

students.remove('Peter')
print(students)

##################################################
new_students = ['Simon','Andrew','Martha','Andrea']
grades = [23, 45, 79, 32]

for i in range(len(new_students)):
    print(new_students[i], 'got the grade', grades[i])


#create list from a string
name = 'Bryson'
letters = list(name)
print(letters)

#create a list from splitting a string
name = 'Bryson Stansfield'
name_parts = name.split()
print(name_parts)
firstname = name_parts[0]
lastname = name_parts[1]
print(lastname.upper(), firstname)