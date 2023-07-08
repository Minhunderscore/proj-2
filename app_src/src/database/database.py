from sqlite3 import connect
import sqlite3

DB_NAME = "database/server.db"

try: 
    connector = connect(DB_NAME)
    cursor = connector.cursor()

    def create_table():
        table_script = '''CREATE TABLE IF NOT EXISTS access_table(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        method VARCHAR(20) NOT NULL,
                        address VARCHAR(12) NOT NULL,
                        time VARCHAR(20) NOT NULL
                    );
                    '''
        cursor.executescript(table_script)
        connector.commit()

    def update_table(data):
        update_query = '''INSERT INTO access_table (method, address, time) VALUES (?, ?, ?);'''
        cursor.execute(update_query, (data["method"], data["ip"], data["time"]))
        connector.commit()

    def get_count():
        count_query = "SELECT COUNT(id) FROM access_table"
        cursor.execute(count_query)
        return cursor.fetchone()[0]

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
