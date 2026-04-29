import psycopg2
from config import load_config

def connect():
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to PostgreSQL')
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    connect()