import mysql.connector
from flask import render_template,request,redirect,url_for
from werkzeug.utils import secure_filename

def deleteStud(id):
    if request.method=="GET":
        return render_template("deletestud.html")
    else:
        action = request.form["action"]
        if action == "Yes":
            con = mysql.connector.connect(host="localhost",user="root",password="rajat@12345",database="SchoolMngmtSys")
            cursor = con.cursor()
            sql = "delete from students where id = %s"
            val = (id,)
            cursor.execute(sql,val)
            con.commit()
        return redirect(url_for("section"))
