import mysql.connector
from flask import render_template, request, redirect, url_for

def fifth():
    if request.method=="GET":
     return render_template("fifth.html")
    else:
       rollno = int(request.form["rollno"]) 
       english=int(request.form["eng"])
       maths=int(request.form["mat"])
       science=int(request.form["sci"])
       social_s=int(request.form["ss"])
       hindi=int(request.form["hin"])
       con=mysql.connector.connect(host="localhost",user="root",password="rajat@12345",database="SchoolMngmtSys")
       cursor =con.cursor()
       total_marks = english + maths + science + social_s + hindi 
       percentage = (total_marks / 500) * 100
       sql="insert into standard_5 (rollno,English,Maths,Science,Social_science,Hindi,percentage) values(%s,%s,%s,%s,%s,%s,%s)"
       val=(rollno,english,maths,science,social_s,hindi,percentage)
       cursor.execute(sql,val)
       con.commit()
       return redirect(url_for("fifth"))