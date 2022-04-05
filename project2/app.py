from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hi everyone'


@app.route('/base')
def home1():
    var="Hola, probando variables"
    return render_template("base.html", var= var) 


if __name__=="__main__":
    app.run()

