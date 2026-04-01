import csv
import psycopg2
from config import load_config


def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    )
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("Table phonebook created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    query = """
    INSERT INTO phonebook (username, phone)
    VALUES (%s, %s)
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (username, phone))
                print("Contact inserted successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)


def insert_from_csv(filename='contacts.csv'):
    query = """
    INSERT INTO phonebook (username, phone)
    VALUES (%s, %s)
    ON CONFLICT (phone) DO NOTHING
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cur.execute(query, (row['username'], row['phone']))
                print("Contacts imported from CSV successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)


def update_contact():
    print("1 - Update username")
    print("2 - Update phone")
    choice = input("Choose option: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    old_username = input("Enter current username: ")
                    new_username = input("Enter new username: ")

                    query = """
                    UPDATE phonebook
                    SET username = %s
                    WHERE username = %s
                    """
                    cur.execute(query, (new_username, old_username))
                    print("Username updated successfully.")

                elif choice == '2':
                    username = input("Enter username: ")
                    new_phone = input("Enter new phone: ")

                    query = """
                    UPDATE phonebook
                    SET phone = %s
                    WHERE username = %s
                    """
                    cur.execute(query, (new_phone, username))
                    print("Phone updated successfully.")

                else:
                    print("Invalid option.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)


def query_contacts():
    print("1 - Show all contacts")
    print("2 - Search by username")
    print("3 - Search by phone prefix")
    choice = input("Choose option: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    cur.execute("SELECT * FROM phonebook ORDER BY id")

                elif choice == '2':
                    username = input("Enter username or part of username: ")
                    cur.execute(
                        "SELECT * FROM phonebook WHERE username ILIKE %s ORDER BY id",
                        ('%' + username + '%',)
                    )

                elif choice == '3':
                    prefix = input("Enter phone prefix: ")
                    cur.execute(
                        "SELECT * FROM phonebook WHERE phone LIKE %s ORDER BY id",
                        (prefix + '%',)
                    )

                else:
                    print("Invalid option.")
                    return

                rows = cur.fetchall()

                if rows:
                    print("\nContacts:")
                    for row in rows:
                        print(row)
                else:
                    print("No contacts found.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)


def delete_contact():
    print("1 - Delete by username")
    print("2 - Delete by phone")
    choice = input("Choose option: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == '1':
                    username = input("Enter username: ")
                    cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
                    print("Contact deleted by username.")

                elif choice == '2':
                    phone = input("Enter phone: ")
                    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                    print("Contact deleted by phone.")

                else:
                    print("Invalid option.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1 - Create table")
        print("2 - Insert from CSV")
        print("3 - Insert from console")
        print("4 - Update contact")
        print("5 - Query contacts")
        print("6 - Delete contact")
        print("0 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_table()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            insert_from_console()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            query_contacts()
        elif choice == '6':
            delete_contact()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == '__main__':
    menu()