password = input("enter password ").strip()
length = True
uc = False
lc = False
digit = False
special = False
p = 0

for characters in password:
    if len(password) >= 6 or len(password) > 28:
        length = True
    else:
        length = False

if length == False:
    print('password must be atleast 6 character and less than 21')

for character in password:
    if character.isupper():
        uc = True
    if character.islower():
        lc = True
    if character.isdigit():
        digit = True
    if not character.isalnum():
        special = True

if lc == True:
    p = p + 1
    #print(p)
if uc == True:
    p = p + 1
    #print(p)
if digit == True:
    p = p + 1
    #print(p)
if special == True:
    p = P = 1
    #print(p)

if length is True and p >= 3:
    print("your password has been accepted")
else:
    print('you need to include', 3 - p, 'of the following')
    if lc == False:
        print('lowercase letter')
    if uc == False:
        print('uppercase letter')
    if digit is False:
        print('number')
    if special is False:
        print('special character')


