# Create and write simple data
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Cherry\n")

print("sample.txt created and already has data")

# Append new lines
with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Orange\n")
    file.write("Mango\n")

print("New lines appended")