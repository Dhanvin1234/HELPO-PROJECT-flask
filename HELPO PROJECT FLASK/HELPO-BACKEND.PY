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
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=='POST':
        connection=sqlite3.connect("helpo.db")
        crsr=connection.cursor()

        Class=request.form["class"]
        password=request.form["password"]
        name=request.form["name"]
        email=request.form["email"]
        print(Class,password,name,email)

        crsr.execute("""INSERT INTO signupdetails(name,class,email,password)VALUES(":name",":Class",":email",":password"),{
            "name":request.form["name"],
            "Class":request.form["Class"],
            "email":request.form["email"],
            "password":request.form["password"],
        }""")
        connection.commit()
        

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
            print("Sorry incorrect credentials")
            
        else:
            return render_template("teacherdashboard.html")


    return render_template("teacherlogin.html")
    


if __name__=="__main__":
    app.run(debug=True)


