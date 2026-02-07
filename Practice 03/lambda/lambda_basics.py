x = lambda a : a + 10
print(x(5)) # 15

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6)) # 30


#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # 13


#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11)) # 22


#Or, use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11)) # 33


#Or, use the same function definition to make both functions, in the same program:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) # 22
print(mytripler(11)) # 22