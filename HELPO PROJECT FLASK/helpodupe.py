from flask import Flask,render_template,request
import sqlite3



app=Flask(__name__,template_folder="TEMPLATES")

@app.route("/",methods=["POST","GET"])
def returner():
    return render_template("helpo.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/signup", methods=["POST","GET"])
def signup():
    if request.method=="POST":
        connection=sqlite3.connect("helpo.db")
        crsr=connection.cursor()
        name=request.form["name"]
        password=request.form["password"]
        email=request.form["email"]



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
if __name__=="__main__":
    app.run(debug=True)
