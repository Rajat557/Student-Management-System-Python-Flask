import mysql.connector
from flask import render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from adminlogin import *

def addDet():
    if request.method == "GET":
        return render_template("addStud.html")
    
    if "uname" in session:
        uname = session["uname"]
    else:
        return redirect(url_for("userHome"))  # Redirect if user is not logged in
    
    rollno = request.form["rollno"] 
    sname = request.form["sname"]
    standard = request.form["sem"]
    gender = request.form["gender"]
    email = request.form["email"]
    number = request.form["number"]
    address = request.form["address"]
    f = request.files['image_url']
    filename = secure_filename(f.filename)
    filename = "static/Images/" + f.filename
    f.save(filename)
    filename = "Images/" + f.filename
    bloodgroup = request.form["bldgrp"]
    
    con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
    cursor = con.cursor()
    if uname == email:
        sql = "insert into students (rollno, sname, standard, gender, email, number, address, image_url, blood_group) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (rollno, sname, standard, gender, email, number, address, filename, bloodgroup)
        cursor.execute(sql, val)
        con.commit()
        return redirect(url_for("userHome"))
    else:
        return redirect(url_for("userHome"))  # Redirect if user email does not match uname
