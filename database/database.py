import sqlite3

connection = sqlite3.connect('../database/main.db')

connection.execute('''CREATE TABLE IF NOT EXISTS USERS (
    ID integer PRIMARY KEY AUTOINCREMENT,
    USERNAME text NOT NULL,
    EMAIL text NOT NULL,
    PASSWORD text NOT NULL);''')

connection.close()


def add_user(username, email, password):
    conn = sqlite3.connect('../database/main.db')
    cursor = conn.cursor()

    data = (username, email, password)
    query = '''INSERT INTO USERS (USERNAME, EMAIL, PASSWORD) VALUES (?, ?, ?);'''

    cursor.execute(query, data)
    conn.commit()

    cursor.close()
    conn.close()


def check_email_address(email):
    conn = sqlite3.connect('../database/main.db')
    cursor = conn.cursor()

    query = '''SELECT * FROM USERS WHERE EMAIL = ?;'''
    cursor.execute(query, (email,))
    conn.commit()

    email_address = cursor.fetchall()

    cursor.close()
    conn.close()

    if not email_address:
        return False
    else:
        return True


def check_username(username):
    conn = sqlite3.connect('../database/main.db')
    cursor = conn.cursor()

    query = '''SELECT * FROM USERS WHERE USERNAME = ?;'''
    cursor.execute(query, (username,))
    conn.commit()

    name = cursor.fetchall()

    cursor.close()
    conn.close()

    if not name:
        return False
    else:
        return True


def validate_user(email_or_username, password):
    conn = sqlite3.connect('../database/main.db')
    cursor = conn.cursor()

    data = (email_or_username, password)

    query = '''SELECT * FROM USERS WHERE EMAIL = ? AND PASSWORD = ?;'''
    cursor.execute(query, data)
    conn.commit()

    user = cursor.fetchall()

    if not user:
        query = '''SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?;'''

        cursor.execute(query, data)
        conn.commit()

        user = cursor.fetchall()

    cursor.close()
    conn.close()

    if not user:
        return False
    else:
        return True


def get_user(email_or_username, password):
    conn = sqlite3.connect('../database/main.db')
    cursor = conn.cursor()

    data = (email_or_username, password)

    query = '''SELECT ID, USERNAME, EMAIL FROM USERS WHERE EMAIL = ? AND PASSWORD = ?;'''
    cursor.execute(query, data)
    conn.commit()

    user = cursor.fetchall()

    if not user:
        query = '''SELECT ID, USERNAME, EMAIL FROM USERS WHERE USERNAME = ? AND PASSWORD = ?;'''

        cursor.execute(query, data)
        conn.commit()

        user = cursor.fetchall()

    cursor.close()
    conn.close()

    return user
