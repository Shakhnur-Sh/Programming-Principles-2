import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="phonebook_db",
        user="postgres",
        password="postgres123",
        port="5432",
        options="-c client_encoding=UTF8"
    )
    print("Connected successfully!")
    conn.close()
    print("Connection closed.")
except Exception as e:
    print("ERROR:", repr(e))