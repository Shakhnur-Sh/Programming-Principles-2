-- Procedure 1: insert or update one contact
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE name = p_name AND surname = p_surname
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO contacts(name, surname, phone)
        VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$;


-- Procedure 2: insert many contacts with phone validation
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_surnames TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9+\-() ]+$' THEN
            IF EXISTS (
                SELECT 1
                FROM contacts
                WHERE name = p_names[i] AND surname = p_surnames[i]
            ) THEN
                UPDATE contacts
                SET phone = p_phones[i]
                WHERE name = p_names[i] AND surname = p_surnames[i];
            ELSE
                INSERT INTO contacts(name, surname, phone)
                VALUES (p_names[i], p_surnames[i], p_phones[i]);
            END IF;
        ELSE
            RAISE NOTICE 'Incorrect data: %, %, %',
                p_names[i], p_surnames[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;


-- Procedure 3: delete contact by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value
       OR phone = p_value;
END;
$$;