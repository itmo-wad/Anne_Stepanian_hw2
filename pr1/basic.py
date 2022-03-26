from flask import Flask, send_from_directory, render_template, request, redirect, url_for, flash, session, make_response
from flask_httpauth import HTTPBasicAuth
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["MONGO_URI"] = "mongodb://localhost:27017/wad"
mongo = PyMongo(app)

@app.route("/", methods=["GET","POST"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        user=mongo.db.users.find({"username":username})

        if user and check_password_hash(user["password"],password):
            return redirect("/profile")
        else:
            return "Error"

    return render_template("auth.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)