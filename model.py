import sqlite3 as sql
from os import path

ROOT = path.dirname(path.realpath(__file__))

def create_post(name,post):
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute(f'INSERT INTO POSTS (Name, Content) VALUES (?,?);',(name,post))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM POSTS;')
    posts = cur.fetchall()
    return posts