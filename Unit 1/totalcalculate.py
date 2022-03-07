# digits = input("Enter your number string: ").strip()
# if digits.isdigit():
#     total = 0
#     for d in digits:
#         total = total + int(d)
#     print(total)
# else:
#     print('Only enter numbers')

earn = input("How many sales")
if earn.isdigit():
    earn = int(earn)
    commision = 0
    if earn >= 10000:
        commision = earn // 100 * 10
        print("Your commision is", commision)

    elif earn < 10000:
        commision = earn // 100 * 5
        print ("Your commision is", commision)


