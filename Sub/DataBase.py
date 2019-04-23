import sqlite3
import os
import libs.Constant as Constant


def Preload():
    try:
        con = sqlite3.connect(os.getcwd() + Constant.Path)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Bot(ROWID INTEGER PRIMARY KEY AUTOINCREMENT, \
        	Title VARCHAR(100) NOT NULL, \
        	ID INTEGER NOT NULL, \
        	Administrator_ID INTEGER)''')

        con.commit()
        cur.close()

        return con

    except Exception as Err:
        print(Err)


def Load():
    try:

        con = Preload()
        cur = con.cursor()
        cur.execute('''SELECT * FROM Bot''')

        Data = cur.fetchall()

        cur.close()
        con.close()

        return Data

    except Exception as Err:
        print(Err)


def Insert(Title, ID, Administrator_ID='NULL'):
    try:

        con = Preload()
        cur = con.cursor()
        cur.execute(f'''INSERT INTO Bot(Title, ID, Administrator_ID) VALUES("{Title}", "{ID}", "{Administrator_ID}")''')

        con.commit()
        cur.close()
        con.close()

    except Exception as Err:
        print(Err)


def GFound(Title):
    try:

        con = Preload()
        cur = con.cursor()
        cur.execute(f'''SELECT Title FROM Bot WHERE Title = "{Title}"''')

        Data = cur.fetchall()

        cur.close()
        con.close()

        return Data

    except Exception as Err:
        print(Err)
