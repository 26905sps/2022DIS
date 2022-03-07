# for i in range(1, 6):
#     line = ''
#     for j in range(1, i + 1):
#         line += str(i)
# print(line)

# for i in range(5):
#     line = ' '
#     for j in range(0,i):
#         line = line + '_'
#     line = line + '#'
#     print(line)

# numbers = '12345'
# for i in range(len(numbers)):
#     line1 = numbers[i]
#     line = ''
#     for j in range(0, i+1):
#         line += line1
#     print(line)

# for i in range(1, 6):
#     line = ''
#     for j in range (0, 5-i):
#         line += '.'
#     for k in range (0, i):
#         line += str(i)
#     print(line)

for i in range(1, 6):
    line = ''
    for j in range(0, 5-i):
        line += '.'
    for k in range(0, 1):
        line += str(i)
    for h in range(0, 2-k):
        line += '.'
    print(line)