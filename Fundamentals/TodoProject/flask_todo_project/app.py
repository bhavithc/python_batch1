
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
next_id = 1

def stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    open_tasks = total - completed
    return total, open_tasks, completed

@app.route("/")
def index():
    total, open_tasks, completed = stats()
    return render_template("index.html",
                           tasks=tasks,
                           total=total,
                           open_tasks=open_tasks,
                           completed=completed)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    title = request.form.get("title","").strip()
    priority = request.form.get("priority","Medium")
    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "priority": priority,
            "completed": False
        })
        next_id += 1
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=8081)
