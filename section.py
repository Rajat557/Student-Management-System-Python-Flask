import mysql.connector
from flask import render_template,request,redirect,url_for

def section():
    if request.method == 'POST':
        standard = request.form['sem']
        #year = request.form['year']

        # Connect to MySQL database
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()

        # Execute search query
        sql = "SELECT * FROM students WHERE standard = %s"
        cursor.execute(sql, (standard,))
        results = cursor.fetchall()

        # Close database connection
        cursor.close()
        con.close()

        return render_template('section.html', results=results)
    else:
        return render_template('section.html')