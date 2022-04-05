from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)


class Myapp(db.Model):
    c_id=db.Column(db.Integer, primary_key=true)
    c_name=db.Column(db.String(500))


@app.route("/")
def home():
    return 'Hi everyone'

@app.route("/insert", methods=["POST"])
def home2():
    c_name=request.form.get("c_name")
    return render_template("base.html", c_name=c_name)

@app.route("/base")
def home1():
    var = "Hello this is a variable"
    return render_template("base.html", var=var)


if __name__=="__main__":
    app.run()