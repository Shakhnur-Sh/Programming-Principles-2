students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students) # [('Tobias', 22), ('Emil', 25), ('Linus', 28)]


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students) # [('Emil', 25), ('Linus', 28), ('Tobias', 22)]


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students) # [('Linus', 28), ('Emil', 25), ('Tobias', 22)]


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[0], reverse=True)
print(sorted_students) # [('Tobias', 22), ('Linus', 28), ('Emil', 25)]