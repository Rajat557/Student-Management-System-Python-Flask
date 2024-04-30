import mysql.connector
from flask import render_template,request,redirect,url_for
from werkzeug.utils import secure_filename

def editStudent1():
    if request.method == "GET":
        con = mysql.connector.connect(host="localhost",user="root",password="rajat@12345",database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = "select * from students where email=%s"
        val = (email,)
        cursor.execute(sql,val)
        student = cursor.fetchone()
        return render_template("userEdit.html",student=student)
    else:
        rollno = request.form["rollno"]
        sname = request.form["sname"]
        standard = request.form["sem"]
        gender = request.form["gender"]
        email = request.form["email"]
        number = request.form["number"]
        address = request.form["address"]
        f=request.files['image_data']
        filename = secure_filename(f.filename)
        filename = "static/Images/"+f.filename
        f.save(filename)
        filename = "Images/"+f.filename
        bloodgroup=request.form["bldgrp"]
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = "UPDATE students SET sname=%s,standard=%s, gender=%s, email=%s, number=%s, address=%s, rollno=%s,image_url=%s,blood_group=%s where email=%s"
        val = (sname,standard,gender, email, number, address, rollno,filename,bloodgroup,id)
        #print(sql, val)
        cursor.execute(sql, val)
        con.commit()
        return redirect(url_for("userHome"))