import psycopg2
from config import load_config

import os
print("RUNNING FILE:", os.path.abspath(__file__))

def connect():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        print("Connected to PostgreSQL successfully.")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("Connection error:", error)
        return None


if __name__ == '__main__':
    conn = connect()
    if conn is not None:
        conn.close()
        print("Connection closed.")