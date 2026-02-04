fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# apple banana 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# apple

for x in range(6):
  print(x)
  if x == 3:
    break
# 0 1 2 3

for x in range(6):
  if x == 3:
    break
  print(x)
# 0 1 2

for x in range(1, 11):
  if x % 2 == 0:
    print(x)
    if x == 6:
      break
# 2 4 6