# Read the whole file
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Using read():")
    print(content)

# Read one line
with open("sample.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    print("Using readline():")
    print(first_line)

# Read all lines into a list
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("Using readlines():")
    print(lines)