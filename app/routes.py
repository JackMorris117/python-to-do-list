from flask import render_template
from app import app
from app.models import User, Task

@app.route("/tasks")
def index():
    user = User.query.get(1)
    tasks = user.tasks
    return render_template("index.html", title="Home", user=user, tasks=tasks)

