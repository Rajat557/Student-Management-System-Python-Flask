import mysql.connector
from flask import render_template,request,redirect,url_for
from adminlogin import *
def profile():
    # Check if user is logged in (you need to implement your login logic here)
    if 'uname' not in session:
        return redirect(url_for('login'))  # Redirect to login page if user is not logged in

    # Retrieve logged-in user's email from session
    user_email = session['email']
    con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
    # Query the database to fetch student profile data based on email
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students WHERE email = %s", (user_email,))
    student_profile = cursor.fetchone()
    cursor.close()

    # Check if student profile exists
    if student_profile:
        # Pass student profile data to HTML template and render it
        return render_template('profile.html', student_profile=student_profile)
    else:
        return "Student profile not found."