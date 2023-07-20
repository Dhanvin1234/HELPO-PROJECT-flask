import sqlite3

connection=sqlite3.connect("helpo.db")
crsr=connection.cursor()
#crsr.execute( """CREATE TABLE teacherlogin (
  #  Class varchar(255) PRIMARY KEY,
    #password varchar(255))""")

#connection.commit()
#connection.close()
def pdetails():
    connection=sqlite3.connect("helpo.db")
    crsr = connection.cursor()
    crsr.execute("INSERT INTO teacherlogin(Class, password) VALUES ('Grade_6', 'ZH9V4X')")
    crsr.execute("INSERT INTO teacherlogin(Class, password) VALUES ('Grade_7', 'P4Q296W')")
    crsr.execute("INSERT INTO teacherlogin(Class, password) VALUES ('Grade_8', 'G6BQI42')")
    crsr.execute("INSERT INTO teacherlogin(Class, password) VALUES ('Grade_9', 'VR93BX3')")
    crsr.execute("INSERT INTO teacherlogin(Class, password) VALUES ('Grade_10', 'HX0D39C')")
    connection.commit()
pdetails()
