from flask import Flask,render_template
app = Flask(__name__)
@app.route("/SA_2")
def mywebpage ():
    return render_template("index.html")
app.run(debug=True)

