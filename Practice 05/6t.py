import re

pattern= r"[ ,\.]" # matches spaces, commas, and dots

text = input("Enter text: ")

result = re.sub(pattern, ":", text) # replace spaces, commas, and dots with colons

print(result)