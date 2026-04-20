import psycopg2
from config import load_config


def connect():
    params = load_config()
    return psycopg2.connect(**params)


def create_table():
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL
            )
        """)

        conn.commit()
        print("Table contacts created successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating table:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def call_upsert(name, surname, phone):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("CALL upsert_contact(%s, %s, %s)", (name, surname, phone))
        conn.commit()
        print("Upsert completed.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in upsert:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def search_pattern(pattern):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        rows = cur.fetchall()

        print("\nSearch results:")
        for row in rows:
            print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in search:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def show_paginated(limit, offset):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()

        print(f"\nPaginated results (limit={limit}, offset={offset}):")
        for row in rows:
            print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in pagination:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def insert_many():
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        names = ['Dana', 'Asel', 'Nurlan']
        surnames = ['Bekova', 'Turgan', 'Kaiyr']
        phones = ['87770001122', 'wrong_phone', '+77015556677']

        cur.execute(
            "CALL insert_many_contacts(%s, %s, %s)",
            (names, surnames, phones)
        )

        conn.commit()
        print("Bulk insert completed.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in bulk insert:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def delete_contact(value):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("CALL delete_contact(%s)", (value,))
        conn.commit()
        print("Delete completed.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in delete:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def show_all_contacts():
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM contacts ORDER BY id")
        rows = cur.fetchall()

        print("\nAll contacts:")
        for row in rows:
            print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while showing contacts:", error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    # Step 1: create table
    create_table()

    # Step 2: test upsert
    call_upsert("Ali", "Nurmukhan", "87011234567")
    call_upsert("Aruzhan", "Serik", "87771234567")
    call_upsert("Ali", "Nurmukhan", "87019999999")

    # Step 3: show all data
    show_all_contacts()

    # Step 4: search by pattern
    search_pattern("Ali")
    search_pattern("8701")
    search_pattern("Ser")

    # Step 5: pagination
    show_paginated(2, 0)
    show_paginated(2, 2)

    # Step 6: bulk insert
    insert_many()
    show_all_contacts()

    # Step 7: delete by name
    delete_contact("Aruzhan")
    show_all_contacts()