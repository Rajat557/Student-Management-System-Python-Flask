import mysql.connector
from flask import render_template,request,redirect,url_for

def addAttend():
    if request.method=="GET":
        return render_template("addattend.html")
    else:
        rollno=request.form["rollno"]
        standard = request.form["sem"]
        attendance=request.form["anum"]
        con=mysql.connector.connect(host="localhost",user="root",password="rajat@12345",database="SchoolMngmtSys")
        cursor =con.cursor()
        sql="insert into attendance (rollno,standard,attendance) values(%s,%s,%s)"
        val=(rollno,standard,attendance)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("adminHome"))