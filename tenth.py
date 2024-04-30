import mysql.connector
from flask import render_template, request, redirect, url_for

def tenth():
    if request.method=="GET":
     return render_template("tenth.html")
    else:
       rollno = request.form["rollno"] 
       english=request.form["eng"]
       maths=request.form["mat"]
       science=request.form["sci"]
       social_s=request.form["ss"]
       hindi=request.form["hin"]
       project=request.form["pro"]
       extra=request.form["exc"]
       con=mysql.connector.connect(host="localhost",user="root",password="rajat@12345",database="SchoolMngmtSys")
       cursor =con.cursor()
       total_marks = english + maths + science + social_s + hindi + project
       percentage = (total_marks / 700) * 100
       sql="insert into standard_10 (rollno,English,Maths,Science,Social_science,Hindi,Project,percentage) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       val=(rollno,english,maths,science,social_s,hindi,project,extra,percentage)
       cursor.execute(sql,val)
       con.commit()
       return redirect(url_for("tenth"))