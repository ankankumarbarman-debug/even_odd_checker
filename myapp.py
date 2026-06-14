from flask import Flask, render_template, request

app = Flask(__name__)

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        return "❌ Weak Password"
    elif score <= 4:
        return "⚠ Medium Password"
    else:
        return "✅ Strong Password"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    password = request.form["password"]
    result = check_password(password)

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Password Result</title>

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,sans-serif;
}}

body{{
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:linear-gradient(-45deg,#ff0080,#7928ca,#2afadf,#00f2fe);
background-size:400% 400%;
animation:bg 10s ease infinite;
}}

@keyframes bg{{
0%{{background-position:0% 50%;}}
50%{{background-position:100% 50%;}}
100%{{background-position:0% 50%;}}
}}

.card{{
background:rgba(255,255,255,0.15);
backdrop-filter:blur(15px);
padding:40px;
border-radius:25px;
text-align:center;
color:white;
box-shadow:0 0 25px rgba(255,255,255,0.3);
animation:float 3s ease-in-out infinite;
}}

@keyframes float{{
0%{{transform:translateY(0px);}}
50%{{transform:translateY(-10px);}}
100%{{transform:translateY(0px);}}
}}

h1{{
font-size:40px;
margin-bottom:20px;
}}

a{{
display:inline-block;
padding:12px 25px;
background:white;
color:#7928ca;
text-decoration:none;
border-radius:10px;
font-weight:bold;
transition:0.3s;
}}

a:hover{{
transform:scale(1.1);
}}

</style>
</head>

<body>

<div class="card">
<h1>{result}</h1>
<a href="/">Check Another Password</a>
</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)
