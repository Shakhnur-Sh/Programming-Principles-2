import re

text = input("Enter text: ")

snake = re.sub(r"[A-Z]", r"_\g<0>", text)  # insert an underscore before each uppercase letter

print("Snake_case:", snake.lower())  # convert the result to lowercase