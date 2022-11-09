import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    data = []
    with open("data/reviews.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", page_title="About", reviews=data)


@app.route("/menu")
def menu():
    data = []
    with open("data/menu.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("menu.html", page_title="Menu", menu=data)


@app.route("/book")
def book():
    return render_template("book.html", page_title="Booking")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
