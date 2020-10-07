from flask import render_template
from app import app


@app.route("/")
def home():
    user = {"username": "Jack"}
    tasks = [
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, cheese, pizza, fruit",
            "done": True
        }
    ]
    return render_template("index.html", title="Home", user=user, tasks=tasks)

