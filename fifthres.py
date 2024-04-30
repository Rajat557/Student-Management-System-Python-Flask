"""import mysql.connector
from flask import render_template, request, redirect, url_for

def result5():
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql =
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.project, s.percentage
        FROM standard_8 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result5.html', results=results)
    else:
        return render_template('result5.html')"""