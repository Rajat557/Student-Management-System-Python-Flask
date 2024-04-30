from flask import Flask,render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = "Firstbit123"
from urls import *


if "__main__" == __name__:
    app.run(debug=True)