a = set('abcdddffaaefg')
print(type(a), a)
sentence = 'Hello to the to my Hello world the'
words = sentence.split()
set_words = set(words)
print(set_words)

if 'Hello' in set_words:
    print('Found')
else:
    print('Not Found')

student_names = {()}
print(type(student_names))