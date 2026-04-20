files = ["database.ini", "config.py", "connect.py", "phonebook.py"]

for file_name in files:
    print(f"\nChecking: {file_name}")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
        print("OK: UTF-8")
    except Exception as e:
        print("ERROR:", e)

        with open(file_name, "rb") as f:
            data = f.read()
        print("Raw bytes:", data)