i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# 1 2 3

count = 0
while count < 5:
    if count == 3:
        break
    print("Count is:", count)
    count += 1
# Count is: 0
# Count is: 1
# Count is: 2

num = 10
while num > 0:
    print(num)
    if num == 6:
        break
    num -= 2
# 10 8 6

n = 5
while n > 0:
    if n == 2:
        break
    print(n)
    n -= 1
# 5 4 3

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
        if i == 6:
            break
    i += 1
# 2 4 6