import sqlite3
from sqlite3 import Error

def create_connection():
    db_file = "nlp.db"
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def login(user_and_pass):
    conn = create_connection()
    with conn:
        username = user_and_pass[0]
        password = user_and_pass[1]
        print('connectoin established')
        cur = conn.cursor()
        sql ="SELECT * FROM users WHERE name='" + username +"' AND password='"+password+"'"
        cur.execute(sql)
        rows = cur.fetchall()
        if len(rows)>0:
            return 'login,Login OK'
        else:
            return 'login,Login fialed'

    return True

def singup(user_and_pass):
    conn = create_connection()
    with conn:
        print('connectoin established')
        cur = conn.cursor()
        # sql ="SELECT * FROM users WHERE name='" + username +"' AND password='"+password+"'"
        sql = ''' INSERT INTO users(name,password)
                      VALUES(?,?) '''
        try:
            cur.execute(sql, user_and_pass)
            if cur.lastrowid > 0:
                return 'singup,Singup OK'
        except Error as e:
            return 'singup,Singup fialed'

    return True
