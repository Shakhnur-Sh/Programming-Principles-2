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