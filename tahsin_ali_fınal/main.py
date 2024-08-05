from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html")

@app.route("/nedir.html")
def nedir():
    return render_template("nedir.html")

@app.route("/etki.html")
def etki():
    return render_template("etki.html")

@app.route("/ciddi.html")
def ciddi():
    return render_template("ciddi.html")

@app.route("/onlem.html")
def onlem():
    return render_template("onlem.html")

if __name__ == "__main__":
    app.run(debug=True)