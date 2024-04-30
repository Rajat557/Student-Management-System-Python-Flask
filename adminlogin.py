from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import base64 

app = Flask(__name__)
app.secret_key = "Firstbit123"


def login():
    if request.method == "GET":
        return render_template("adminlogin.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        sql = '''select count(*) from admininfo where username=%s and password=%s and role=%s'''
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        val = (uname, pwd, 'admin')
        cursor.execute(sql, val)
        count = cursor.fetchone()
        if int(count[0]) == 1:
            session["uname"] = uname
            return redirect("/adminHome")
        else:
            return redirect(url_for("login"))



def adminHome():
    if "uname" in session:
        return render_template("adminHome.html")
    else:
        return redirect(url_for("login"))
    
def login1():
    if request.method == "GET":
        return render_template("userlogin.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        sql = '''select count(*) from userinfo where email=%s and password=%s'''
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        val = (uname, pwd,)
        cursor.execute(sql, val)
        count = cursor.fetchone()
        if int(count[0]) == 1:
            session["uname"] = uname
            return redirect("/userHome")
        else:
            return redirect(url_for("login1"))  



def userHome():
    if "uname" in session:
        return render_template("userHome.html")
    else:
        return redirect(url_for("login1"))    

def Logout():
    session.clear()
    return redirect("/")

""""uname = request.form["uname"]
def profile():
    uname = request.form["uname"]
    # Check if user is logged in
    if 'uname' not in session:
        return redirect(url_for('userhome'))  # Redirect to login page if user is not logged in
    
    # Retrieve logged-in user's email from session
    user_email = session['uname']
    
    # Connect to the database
    con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
    cursor = con.cursor()

    # Query the database to fetch student profile data based on email
    cursor.execute("SELECT * FROM students WHERE email = %s", (user_email,))
    student_profile = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    con.close()

    # Check if student profile exists
    if student_profile:
        # Pass student profile data to HTML template and render it
        return render_template('profile.html', student_profile=student_profile)
    else:
        return "Student profile not found."""""

def profile():
        if "uname" in session:
            uname = session["uname"]
            con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
            sql="select * from students where email=%s"
            cursor = con.cursor()
            val = (uname,)
            cursor.execute(sql, val)
            profiles = cursor.fetchall()
            cursor.close()
            con.close()

            return render_template('profile.html', profiles=profiles)
        
            
def register():
    if request.method == "GET":
            return render_template("register.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        pwd1 = request.form["pwd1"]
        if pwd == pwd1:
            con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
            cursor = con.cursor()
            sql = "insert into userinfo (email,password) values(%s, %s)"
            val = (uname,pwd)
            cursor.execute(sql, val)
            con.commit()
            return redirect(url_for("login1"))
        else:  
          return"Passwords do not match. Please try again.",redirect(url_for("register"))
        
            