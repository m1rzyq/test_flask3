from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("welcome.html", username=request.form.get("username"))

if __name__ == "__main__":
    app.run(debug=True)