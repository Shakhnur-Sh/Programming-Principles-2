import psycopg2
import csv
import json
from config import load_config


def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


def run_sql_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            sql = file.read()

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()

        print(filename, 'was executed successfully.')
    except Exception as error:
        print('Error:', error)


def get_group_id(cur, group_name):
    cur.execute(
        "INSERT INTO groups(name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
        (group_name,)
    )

    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    group_id = cur.fetchone()[0]

    return group_id


def add_contact():
    name = input('Name: ')
    email = input('Email: ')
    birthday = input('Birthday YYYY-MM-DD: ')
    group_name = input('Group: ')
    phone = input('Phone: ')
    phone_type = input('Phone type home/work/mobile: ')

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                group_id = get_group_id(cur, group_name)

                cur.execute(
                    """
                    INSERT INTO contacts(name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                    """,
                    (name, email, birthday, group_id)
                )

                contact_id = cur.fetchone()[0]

                cur.execute(
                    "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
                    (contact_id, phone, phone_type)
                )

                conn.commit()
                print('Contact added.')
    except Exception as error:
        print('Error:', error)


def show_contacts():
    sort = input('Sort by name/birthday/date: ')

    if sort == 'birthday':
        order_by = 'c.birthday'
    elif sort == 'date':
        order_by = 'c.date_added'
    else:
        order_by = 'c.name'

    sql = f"""
        SELECT c.name, c.email, c.birthday, g.name, c.date_added
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY {order_by}
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    except Exception as error:
        print('Error:', error)


def filter_by_group():
    group_name = input('Group name: ')

    sql = """
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
        ORDER BY c.name
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (group_name,))
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    except Exception as error:
        print('Error:', error)


def search_by_email():
    email_part = input('Search email: ')

    sql = """
        SELECT name, email, birthday
        FROM contacts
        WHERE email ILIKE %s
        ORDER BY name
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, ('%' + email_part + '%',))
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    except Exception as error:
        print('Error:', error)


def search_all_fields():
    query = input('Search name/email/phone/group: ')

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM search_contacts(%s)", (query,))
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    except Exception as error:
        print('Error:', error)


def add_phone_console():
    name = input('Contact name: ')
    phone = input('New phone: ')
    phone_type = input('Phone type home/work/mobile: ')

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, phone_type))
                conn.commit()
                print('Phone added.')
    except Exception as error:
        print('Error:', error)


def move_group_console():
    name = input('Contact name: ')
    group_name = input('New group: ')

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("CALL move_to_group(%s, %s)", (name, group_name))
                conn.commit()
                print('Contact moved.')
    except Exception as error:
        print('Error:', error)


def pagination_console():
    page_size = 3
    page = 0

    while True:
        offset = page * page_size

        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    # This uses the DB pagination function.
                    cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (page_size, offset))
                    rows = cur.fetchall()

                    print('\nPage:', page + 1)
                    for row in rows:
                        print(row)

        except Exception as error:
            print('Error:', error)
            break

        command = input('next / prev / quit: ')

        if command == 'next':
            page = page + 1
        elif command == 'prev':
            if page > 0:
                page = page - 1
        elif command == 'quit':
            break


def export_to_json():
    filename = input('JSON filename: ')

    sql = """
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.name
    """

    try:
        contacts = []

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()

                for row in rows:
                    contact_id = row[0]

                    cur.execute(
                        "SELECT phone, type FROM phones WHERE contact_id = %s",
                        (contact_id,)
                    )
                    phone_rows = cur.fetchall()

                    phones = []
                    for phone_row in phone_rows:
                        phones.append({
                            'phone': phone_row[0],
                            'type': phone_row[1]
                        })

                    contact = {
                        'name': row[1],
                        'email': row[2],
                        'birthday': str(row[3]),
                        'group': row[4],
                        'phones': phones
                    }

                    contacts.append(contact)

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(contacts, file, indent=4)

        print('Exported to JSON.')

    except Exception as error:
        print('Error:', error)


def insert_contact_from_json(cur, contact):
    name = contact['name']
    email = contact['email']
    birthday = contact['birthday']
    group_name = contact['group']

    group_id = get_group_id(cur, group_name)

    cur.execute(
        """
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (name, email, birthday, group_id)
    )

    contact_id = cur.fetchone()[0]

    for phone in contact['phones']:
        cur.execute(
            "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
            (contact_id, phone['phone'], phone['type'])
        )


def import_from_json():
    filename = input('JSON filename: ')

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contacts = json.load(file)

        with get_connection() as conn:
            with conn.cursor() as cur:
                for contact in contacts:
                    name = contact['name']

                    cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
                    found = cur.fetchone()

                    if found:
                        answer = input(name + ' already exists. skip or overwrite? ')

                        if answer == 'skip':
                            continue

                        if answer == 'overwrite':
                            cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
                            insert_contact_from_json(cur, contact)
                    else:
                        insert_contact_from_json(cur, contact)

                conn.commit()

        print('Imported from JSON.')

    except Exception as error:
        print('Error:', error)


def import_from_csv():
    filename = input('CSV filename: ')

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            with get_connection() as conn:
                with conn.cursor() as cur:
                    for row in reader:
                        name = row['name']
                        email = row['email']
                        birthday = row['birthday']
                        group_name = row['group']
                        phone = row['phone']
                        phone_type = row['type']

                        group_id = get_group_id(cur, group_name)

                        cur.execute("SELECT id FROM contacts WHERE name = %s", (name,))
                        found = cur.fetchone()

                        if found:
                            contact_id = found[0]
                            cur.execute(
                                """
                                UPDATE contacts
                                SET email = %s, birthday = %s, group_id = %s
                                WHERE id = %s
                                """,
                                (email, birthday, group_id, contact_id)
                            )
                        else:
                            cur.execute(
                                """
                                INSERT INTO contacts(name, email, birthday, group_id)
                                VALUES (%s, %s, %s, %s)
                                RETURNING id
                                """,
                                (name, email, birthday, group_id)
                            )
                            contact_id = cur.fetchone()[0]

                        cur.execute(
                            "INSERT INTO phones(contact_id, phone, type) VALUES (%s, %s, %s)",
                            (contact_id, phone, phone_type)
                        )

                    conn.commit()

        print('Imported from CSV.')

    except Exception as error:
        print('Error:', error)


def menu():
    while True:
        print('\nPHONEBOOK MENU')
        print('1 - Run schema.sql')
        print('2 - Run procedures.sql')
        print('3 - Add contact')
        print('4 - Show contacts')
        print('5 - Filter by group')
        print('6 - Search by email')
        print('7 - Search all fields')
        print('8 - Pagination')
        print('9 - Add phone')
        print('10 - Move to group')
        print('11 - Export to JSON')
        print('12 - Import from JSON')
        print('13 - Import from CSV')
        print('0 - Exit')

        choice = input('Choose: ')

        if choice == '1':
            run_sql_file('schema.sql')
        elif choice == '2':
            run_sql_file('procedures.sql')
        elif choice == '3':
            add_contact()
        elif choice == '4':
            show_contacts()
        elif choice == '5':
            filter_by_group()
        elif choice == '6':
            search_by_email()
        elif choice == '7':
            search_all_fields()
        elif choice == '8':
            pagination_console()
        elif choice == '9':
            add_phone_console()
        elif choice == '10':
            move_group_console()
        elif choice == '11':
            export_to_json()
        elif choice == '12':
            import_from_json()
        elif choice == '13':
            import_from_csv()
        elif choice == '0':
            break
        else:
            print('Wrong choice.')


if __name__ == '__main__':
    menu()