values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
roman = "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
numerals = ""
number = int(input("Number between 1 and 3999"))
if number in range(0, 4000):
    for i in range(13):
        while number >= values[i]:
            number = number - values[i]
            numerals += roman[i]
else:
    print("number is not in the range")
print(numerals)
