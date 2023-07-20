from multiprocessing import connection
from flask import Flask,render_template,request
import sqlite3



app=Flask(__name__,template_folder="TEMPLATES")

@app.route("/",methods=["POST","GET"])
def returner():
    return render_template("helpo.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/about")
def about():
    return render_template("aboutus.html")
@app.route("/ask")
def ask():
    return render_template("askaquestions.html")
@app.route("/helpo")
def helpo():
    return render_template("helpo.html")
@app.route("/teach",methods=['GET','POST'])
def teach():

    if request.method=='POST':
        connection=sqlite3.connect("helpo.db")
        crsr=connection.cursor()

        Class=request.form["name"]
        password=request.form["password"]
        print(Class,password)
        query="SELECT Class,password FROM teacherlogin where Class='"+Class+"'and password='"+password+"'"
        crsr.execute(query)
        results=crsr.fetchall()
        
        if len(results)==0:
            print("BOZO incorrect credentials")
            return render_template("teacherloginwrong.html")
        else:
            return render_template("teacherdashboard.html")

    if request.method=='POST':
        connection=sqlite3.connect("helpo.db")
        crsr=connection.cursor()

        Class=request.form["name"]
        password=request.form["password"]
        print(Class,password)
        querry="SELECT Class,password FROM teacherloginwrong where Class='"+Class+"'and password='"+password+"'"
        crsr.execute(querry)
        results=crsr.fetchall()
        
        connection.commit()

        if len(results)==0:
            print(" incorrect credentials")
            return render_template("teacherloginwrong.html")
        else:
            return render_template("teacherdashboard.html")

        




    return render_template("teacherlogin.html")
    


if __name__=="__main__":
    app.run(debug=True)


