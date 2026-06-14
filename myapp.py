from flask import Flask, render_template, request

app = Flask(__name__)

def check_password(password):

    if len(password) < 8:
        return "🔴 Weak Password"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(char in special_chars for char in password)

    if has_upper and has_lower and has_digit and has_special:
        return "🟢 Strong Password"

    elif (has_upper or has_lower) and has_digit:
        return "🟡 Medium Password"

    else:
        return "🔴 Weak Password"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    password = request.form["password"]

    result = check_password(password)

    return f"""
    <h1>{result}</h1>
    <a href="/">Check Another Password</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
