fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# apple cherry

for x in range(6):
  if x == 3:
    continue
  print(x)
# 0 1 2 4 5

for x in range(1, 11):
  if x % 2 != 0:
    continue
  print(x)
# 2 4 6 8 10

for x in fruits:
  if "a" in x:
    continue
  print(x)
# (No output, all fruits contain "a")

for x in range(10):
  if x < 5:
    continue
  print(x)
# 5 6 7 8 9