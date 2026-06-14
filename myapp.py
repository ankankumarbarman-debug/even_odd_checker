from flask import Flask, render_template, request

app = Flask(__name__)

def odd_even(num):
    if num % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():

    num = int(request.form["number"])

    if num < 0:
        result = "Number is Negative"
    elif num == 0:
        result = "Number is Zero"
    else:
        result = odd_even(num)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Result</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:100px;">
        <h1>{result}</h1>
        <a href="/">Check Another Number</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)