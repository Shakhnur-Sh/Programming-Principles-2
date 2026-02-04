i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# 1 2 4 5 6

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count is:", count)
# Count is: 1
# Count is: 2
# Count is: 4

num = 10
while num > 0:
    num -= 2
    if num == 6:
        continue
    print(num)
# 8 4 2 0

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
# 4 3 1 0

i = 1
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)
# 2 4 6 8 10