import re

text = input("Enter text: ")

pattern = r'(?=[A-Z])'  # matches positions before uppercase letters

result = re.split(pattern, text)  # split the text at uppercase letters

print(result)