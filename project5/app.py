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
    new_c_name=Myapp(c_name=c_name)
    db.session.add(new_c_name)
    db.session.commit()

    return redirect(url_for("home1"))



    return redirect(url_for("home1"))


@app.route("/base")
def home1():
    my_list=Myapp.query.all()
    var ="Hello this is a varible"
    return render_template("base.html", var=var, my_list=my_list)


if __name__=="__main__":
    app.run()