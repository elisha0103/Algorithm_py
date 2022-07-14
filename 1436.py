n = int(input())
count = 0
num = '666'
title = ['6','6','6']

while True:
    if num.find('666') != -1:
        count +=1
    if n == count:
        break
    num = int(num) + 1
    num = str(num)

print(num)
