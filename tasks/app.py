from flask import Flask, request, redirect, jsonify, render_template_string

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Study OpenShift", "done": False},
    {"id": 2, "title": "Pass EX288", "done": False},
]

PAGE = """
<!doctype html>
<html>
<head>
    <title>EX288 Tasks</title>
</head>
<body>
    <h1>EX288 Tasks</h1>

    <form method="POST" action="/tasks">
        <input name="title" placeholder="New task" required>
        <button type="submit">Add</button>
    </form>

    <ul>
    {% for task in tasks %}
        <li>
            {{ task["title"] }}
            {% if task["done"] %}
                [done]
            {% else %}
                <form method="POST"
                      action="/tasks/{{ task['id'] }}/done"
                      style="display:inline">
                    <button type="submit">Done</button>
                </form>
            {% endif %}
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(PAGE, tasks=tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.form.get("title")

    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    })

    return redirect("/")

@app.route("/tasks/<int:task_id>/done", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True

    return redirect("/")

@app.route("/api/tasks")
def api_tasks():
    return jsonify(tasks)

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

app.run(host="0.0.0.0", port=8080)