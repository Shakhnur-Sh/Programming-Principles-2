a = 5
b = 2
if a > b: print("a is greater than b") # a is greater than b


a = 2
b = 330
print("A") if a > b else print("B") # B because b is greater than a


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger) # Bigger is 20


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 
# =  will come because a == b

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value) # Maximum value: 20


username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name) # Welcome, Guest