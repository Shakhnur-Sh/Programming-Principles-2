import re

pattern = r"a.*b" # a followed by any characters (including none) and then b

text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")