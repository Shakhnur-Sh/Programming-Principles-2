# Iterate through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# apple banana cherry


# Iterate through a string
for x in "banana":
  print(x)
# b a n a n a


# Loop through a range of numbers
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana


# Loop through a range of numbers
for x in [0, 1, 2]:
  pass
# (No output, just a pass statement)