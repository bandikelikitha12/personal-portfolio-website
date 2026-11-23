from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        password = request.form.get("password", "")
        result = check_password(password)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)