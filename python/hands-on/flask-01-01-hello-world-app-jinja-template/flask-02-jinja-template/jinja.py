import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html",number1=5,number2=10 )

@app.route("/mult")
def number():
    num1=2
    num2=4
    return render_template("body.html",value1=num1,value2=num2,value3=num1*num2)
if __name__=="__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0",port=80)
    