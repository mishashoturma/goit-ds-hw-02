import sqlite3

def create_db():
    with open('table.sql', 'r') as f:
        sql = f.read()
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()