coded_msg = input('enter msg')
msg = ''
words = coded_msg.split()
for word in words:
    if word.isupper():
        msg = msg + word + ''

print(msg)
