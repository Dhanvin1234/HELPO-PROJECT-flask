import sqlite3

connection=sqlite3.connect("helpo.db")
crsr=connection.cursor()
crsr.execute( """CREATE TABLE signupdetails (
    name text,
    class varchar(255),
    email varchar(255) PRIMARY KEY,
    password varchar(255))""")


connection.commit()
#connection.close()
def pdetails():
    connection=sqlite3.connect("helpo.db")
    crsr = connection.cursor()
#    crsr.execute("INSERT INTO signupdetails VALUES (:name, :email, :password)")
connection.commit()