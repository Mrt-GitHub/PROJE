from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/second")
def ikinci():
    return "Hello again"

@app.route("/forth/<int:id>")
def forth(id):
    return f"Id of this page is {id}"

if __name__=="__main__":
    # app.run(debug=True, port=2000)
    app.run(host="0.0.0.0",port=80)