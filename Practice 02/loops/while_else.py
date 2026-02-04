i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# 1 2 3 4 5
# i is no longer less than 6

count = 0
while count < 5:
  print("Count is:", count)
  count += 1
else:
  print("Counting complete")
# Count is: 0
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4
# Counting complete

num = 10
while num > 0: 
  print(num)
  num -= 2
else:
  print("num is no longer greater than 0")
# 10 8 6 4 2
# num is no longer greater than 0

n = 5
while n > 0:
  print(n)
  n -= 1
else:
    print("n has reached zero")
# 5 4 3 2 1
# n has reached zero

i = 1
while i <= 10:
  if i % 2 == 0:
    print(i)
  i += 1
else:
  print("Finished printing even numbers up to 10")
# 2 4 6 8 10
# Finished printing even numbers up to 10