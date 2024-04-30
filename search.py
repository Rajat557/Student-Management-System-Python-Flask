import mysql.connector
from flask import render_template,request,redirect,url_for

def search():
    if request.method == 'POST':
        rollno = request.form['rollno']
        standard = request.form['sem']

        # Connect to MySQL database
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()

        # Execute search query
        sql = "SELECT * FROM students WHERE rollno = %s AND standard = %s"
        cursor.execute(sql, (rollno, standard))
        results = cursor.fetchall()

        # Close database connection
        cursor.close()
        con.close()

        return render_template('search.html', results=results)
    else:
        return render_template('search.html')