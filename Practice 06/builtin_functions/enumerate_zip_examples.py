names = ["Ali", "Aruzhan", "Dana"]
scores = [85, 92, 78]

# enumerate()
for index, name in enumerate(names, start=1):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# Built-in functions
print("Length:", len(scores))
print("Sum:", sum(scores))
print("Minimum:", min(scores))
print("Maximum:", max(scores))
print("Sorted scores:", sorted(scores))

#enumerate() is used to get both index and value while iterating over a list, starting from 1 in this case.
#zip() is used to combine two lists (names and scores) into pairs for iteration.