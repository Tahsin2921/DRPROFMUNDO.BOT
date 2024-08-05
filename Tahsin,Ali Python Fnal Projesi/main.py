from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/nedir")
def nedir():
    return render_template("nedir.html")

app.run(debug=True)