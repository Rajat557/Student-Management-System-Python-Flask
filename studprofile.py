import mysql.connector
from flask import render_template,request,redirect,url_for

def Sprofile():
    if "uname" in session: