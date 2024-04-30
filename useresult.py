import mysql.connector
from flask import render_template, request, redirect, url_for
def result():
    if request.method=="POST":
        sem = request.form['sem']
        if sem == "5":
            return result5()
        elif sem == "6":
            return result6()
    return render_template('result.html')

def result5():
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = """
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.percentage
        FROM standard_5 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        """
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result5.html', results=results)
    else:
        return render_template('result5.html')

def result6():
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = """
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.project, s.percentage
        FROM standard_6 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        """
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result.html', results=results)
    else:
        return render_template('result.html')

def result7():
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = """
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.project, s.percentage
        FROM standard_7 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        """
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result.html', results=results)
    else:
        return render_template('result.html')    

def result8():
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = """
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.project, s.percentage
        FROM standard_8 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        """
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result.html', results=results)
    else:
        return render_template('result.html')
    
def result9():    
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = """
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.project, s.percentage
        FROM standard_9 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        """
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result.html', results=results)
    else:
        return render_template('result.html')
    
def result10():    
    if request.method=="POST":
        rollno = request.form['rollno']
        standard=request.form['sem']
        con = mysql.connector.connect(host="localhost", user="root", password="rajat@12345", database="SchoolMngmtSys")
        cursor = con.cursor()
        sql = """
        SELECT st.sname, s.rollno, s.standard, s.english, s.maths, s.science, s.social_science, s.hindi, s.project,s.extra_curriculum, s.percentage
        FROM standard_9 s
        JOIN students st ON s.rollno = st.rollno AND s.standard = st.standard
        WHERE s.rollno = %s AND s.standard = %s
        """
        cursor.execute(sql, (rollno,standard,))
        results = cursor.fetchall()
        cursor.close()
        con.close()
        return render_template('result10.html', results=results)
    else:
        return render_template('result10.html')    