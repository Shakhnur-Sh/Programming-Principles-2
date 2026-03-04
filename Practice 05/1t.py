import re

pattern = r"ab*" # a followed by zero or more b's

text = input("Enter a string: ")

if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")