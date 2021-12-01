from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("welcome.html", username=request.form.get("username"))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')