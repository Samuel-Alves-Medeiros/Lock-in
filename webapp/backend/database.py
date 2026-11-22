import sqlite3

sessions = 7
email = "piripapo@gmail.com"

def connect_database():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tasks_table():
    conn = connect_database()
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")
    query = """CREATE TABLE IF NOT EXISTS pomo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    completed_at TEXT DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
      )"""
    cursor.execute(query)
    conn.commit()
    conn.close()

create_tasks_table()

# def get_id(email):
#   conn = connect_database()
#   cursor = conn.cursor()
#   query = "SELECT id, name, password FROM users WHERE email = ?"
#   data = cursor.execute(query, (email,)).fetchone()
#   conn.commit()
#   conn.close()
#   return data["id"]

# def inserir_pomo_session(sessions):
#   conn = connect_database()
#   cursor = conn.cursor()
#   query = "INSERT INTO pomo (user_id, sessions) VALUES (?, ?)"
#   cursor.execute(query, (get_id(),sessions,))
#   conn.commit()
#   conn.close()

# inserir_pomo_session(sessions) 