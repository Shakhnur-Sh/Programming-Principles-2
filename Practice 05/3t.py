import re

pattern = r"[a-z]+_[a-z]+" # lowercase letters joined with a underscore

text = input("Enter text: ")

matches = re.findall(pattern, text)

print("Matches:", matches)