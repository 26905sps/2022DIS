# name = input('enter name')
# while name != 'QUIT':
#     print(name)
#     name = input('enter name')

# N = int(input('number'))
# i = 0
# while i < N:
#     i = i + 1
#     print(str(i) + '*')

# n = int(input('enter number'))
# while n != 1:
#     print(n)
#     if n % 2 == 0:
#         n = n / 2
#     else:
#         n = n * 3 + 1
# print(n)

# p = 2600000
# years = 0
# while p < 5000000:
#     n = p * 0.3 / 10
#     p = p + n
#     years += 1
# print(int(p))
# print(years)

num1 = int(input('enter number 1'))
num2 = int(input('enter number 2'))
if num1 >= num2:
    ln = num1
    sn = num2
else:
    ln = num2
    sn = num1

while sn != 0:
    remainder = ln % sn
    ln = sn
    sn = remainder

print('GCD of', num1, 'and', num2, 'is', ln)
