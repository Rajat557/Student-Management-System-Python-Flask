import mysql.connector
from flask import render_template, request, redirect, url_for

def nineth():
    if request.method == "GET":
        return render_template("nineth.html")
    else:
        rollno = request.form["rollno"] 
        english = int(request.form["eng"])  # Convert to integer
        maths = int(request.form["mat"])  # Convert to integer
        science = int(request.form["sci"])  # Convert to integer
        social_s = int(request.form["ss"])  # Convert to integer
        hindi = int(request.form["hin"])  # Convert to integer
        project = int(request.form["pro"])  # Convert to integer
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        total_marks = english + maths + science + social_s + hindi + project
        percentage = (total_marks / 600) * 100
        sql = "insert into standard_9 (rollno, English, Maths, Science, Social_science, Hindi, Project, percentage) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (rollno, english, maths, science, social_s, hindi, project, percentage)
        cursor.execute(sql, val)
        con.commit()
        return redirect(url_for("nineth"))