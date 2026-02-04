for x in range(6):
  print(x)
else:
  print("Finally finished!")
# 0 1 2 3 4 5
# Finally finished!

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# 0 1 2

for x in ["apple", "banana", "cherry"]:
  print(x)
else:
  print("No more fruits!")
# apple banana cherry
# No more fruits!

for x in ["apple", "banana", "cherry"]:
  if x == "banana": break
  print(x)
else:
    print("No more fruits!")
# apple

for x in range(1, 6):
  print(x)
else:
  print("Counting completed!")
# 1 2 3 4 5
# Counting completed!