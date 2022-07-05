import sqlite3 as sql


username = "Sam"
password = "123abc"
con = sql.connect("data.db")
cur = con.cursor()
statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
cur.execute(statement)
if not cur.fetchone(): 
    print("Login failed")
else:
    print("Welcome")