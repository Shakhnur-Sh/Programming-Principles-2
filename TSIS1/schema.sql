DROP TABLE IF EXISTS phones;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS groups;

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
);

INSERT INTO groups(name)
VALUES ('Family'), ('Work'), ('Friend'), ('Other')
ON CONFLICT (name) DO NOTHING;

-- Optional pagination function.
-- If you already have this function from Practice 8, you can skip this part.
CREATE OR REPLACE FUNCTION get_contacts_page(p_limit INT, p_offset INT)
RETURNS TABLE(
    contact_name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    date_added TIMESTAMP
)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, c.birthday, g.name, c.date_added
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    ORDER BY c.name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;