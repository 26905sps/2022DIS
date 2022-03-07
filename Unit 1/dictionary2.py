student_grades = {
    "Simon": 45,
    "Alison": 78,
    "John": 72,
    "Tracy": 83,
    "Zac": 22
}

print(type(student_grades))
print(student_grades)

# print the student names and their grades
for k, v in student_grades.items():
    print(k,'got:', v)

# ask for a name and return the grade or 'not found'
name = input('enter name')
if name in student_grades:
    print(name, 'got:', student_grades[name])
else:
    print('Name not found')

# print a list of all the student names -> ie the keys
print(list(student_grades.keys()))

# print a list of all the grades -> ie the values
print(list(student_grades.values()))

# sort the dictionary according to student names -> ie the keys
print(sorted(student_grades.keys()))

# sort the dictionary according to the grades -> ie the values
print(sorted(student_grades.values()))

# sort the dictionary in reverse order of student names
print(list(reversed(sorted(student_grades.keys()))))