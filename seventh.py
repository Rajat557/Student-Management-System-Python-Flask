import mysql.connector
from flask import render_template, request, redirect, url_for

def seventh():
    if request.method=="GET":
     return render_template("seventh.html")
    else:
       rollno = request.form["rollno"] 
       english=request.form["eng"]
       maths=request.form["mat"]
       science=request.form["sci"]
       social_s=request.form["ss"]
       hindi=request.form["hin"]
       project=request.form["pro"]
       con=mysql.connector.connect(host="localhost",user="root",password="rajat@12345",database="SchoolMngmtSys")
       cursor =con.cursor()
       total_marks = english + maths + science + social_s + hindi + project
       percentage = (total_marks / 600) * 100
       sql="insert into standard_7 (rollno,English,Maths,Science,Social_science,Hindi,Project,percentage) values(%s,%s,%s,%s,%s,%s,%s,%s)"
       val=(rollno,english,maths,science,social_s,hindi,project,percentage)
       cursor.execute(sql,val)
       con.commit()
       return redirect(url_for("seventh"))