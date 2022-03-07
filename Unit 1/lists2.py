names = []
username = input('Enter your name or quit: ').strip()
while username.lower() != 'quit':
    if username.title() not in names:
        names.append(username.title())
    else:
        print('That name already exists')
    username = input('Enter your name or quit: ').strip()

if len(names) > 0:
    names.sort()
    for name in names:
        print(name)

else:
    print('There are no names to show')

