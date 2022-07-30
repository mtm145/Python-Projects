
import sqlite3
from sqlite3 import Error

database = r"F:\Estudos\python\pooTest\bancosqlite.db"


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn


def create_table(conn, table_sql):
    try:
        c = conn.cursor()
        c.execute(table_sql)

    except Error as e:
        print(e)


def insert_table(conn, insert_data_sql):
    try:
        c = conn.cursor()
        c.execute(insert_data_sql)
        conn.commit()

    except Error as e:
        print(e)


def drop_table(conn, drop_table_sql):
    try:
        c = conn.cursor()
        c.execute(drop_table_sql)

    except Error as e:
        print(e)


def main():
    database = r"F:\Estudos\python\pooTest\bancosqlite.db"

    conn = create_connection(database)

    if conn is not None:
        pass

    else:
        print("Problema de conexão com o banco de dados!")


'''conn = create_connection(database)

c = conn.cursor()
c.execute("SELECT * FROM pessoas")
print(c.fetchall())'''
