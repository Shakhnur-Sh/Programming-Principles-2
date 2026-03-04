import re

text = input("Enter text: ")

words=text.split("_")

camel=words[0]

for word in words[1:]:
    camel+=word.capitalize()

print("CamelCase:", camel)

# converting snake_case to camelCase