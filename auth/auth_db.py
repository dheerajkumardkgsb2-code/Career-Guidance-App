import sqlite3

def create_db():
    conn = sqlite3.connect('auth/users.db')
    cursor = conn.cursor()
    
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()
