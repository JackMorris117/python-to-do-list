from app import app


@app.route("/<name>")
def home(name):
    return f"Hello {name.upper()}!"

