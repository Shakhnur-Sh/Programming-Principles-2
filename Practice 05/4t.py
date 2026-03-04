import re

pattern = r"[A-Z][a-z]+" # one upper case letter followed by lower case letters

text = input("Enter text: ")

matches = re.findall(pattern, text)

print("Matches:", matches)