import mysql.connector
from flask import render_template, request, redirect, url_for

def showstd():
    return render_template("marks.html")
