import re

pattern = r"ab{2,3}" # a followed by 2 or 3 b's

text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")