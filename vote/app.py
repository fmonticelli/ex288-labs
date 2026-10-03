from flask import Flask, request, redirect, jsonify, render_template_string

app = Flask(__name__)

votes = {
    "cats": 0,
    "dogs": 0
}

PAGE = """
<!doctype html>
<html>
<head>
    <title>EX288 Voting App v2</title>
</head>
<body>
    <h1>EX288 Voting App v2</h1>

    <form method="POST" action="/vote">
        <button name="option" value="cats">Cats</button>
        <button name="option" value="dogs">Dogs</button>
    </form>

    <h2>Results</h2>
    <p>Cats: {{ votes["cats"] }}</p>
    <p>Dogs: {{ votes["dogs"] }}</p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(PAGE, votes=votes)

@app.route("/vote", methods=["POST"])
def vote():
    option = request.form.get("option")

    if option in votes:
        votes[option] += 1

    return redirect("/")

@app.route("/results")
def results():
    return jsonify(votes)

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

app.run(host="0.0.0.0", port=8080)