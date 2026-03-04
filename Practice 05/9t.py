import re

text = input("Enter camelCase text: ")

result=re.sub(r"([A-Z])", r" \1", text) # insert a space before each uppercase letter

print(result)