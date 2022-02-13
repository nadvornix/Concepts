import json
import builtins
from itertools import count
from flask import Flask, render_template, request
app = Flask(__name__)
"""
Notes:
- it may be useful to put date_created to datastore.json.
- Give indexes/keys to names of ideas, so you can rename them.
"""

datastore_fn = "datastore.json"


@app.route("/")
def index():
    return "Hello World!"


def find_free_id(data):
    "n: brutish..."
    for i in count():
        if not str(i) in data:
            return i


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        ideas = request.form.getlist("ideas")
        #filter empty:
        ideas = [idea for idea in ideas if idea.strip()]
        name = request.form["name"]
        print(ideas, name)
        try:
            with open(datastore_fn, "r+") as f:
                data = json.load(f)
        except (json.decoder.JSONDecodeError, builtins.FileNotFoundError):
            data = {}
        new_id = find_free_id(data)
        new_item = {"name": name,
                        "ideas": ideas,
                        "id": new_id
                        }
        data[new_id] = new_item
        with open(datastore_fn, "w") as f:
            json.dump(data, f, indent=4)
        return render_template("poll_created.html", new_item=new_item)

    else:
        print(request.method)
    return render_template("create.html")


@app.route("/participant/<int:poll_id>", methods=["GET", "POST"])
def submit(poll_id):
    if request.method == "POST":
        print(request.form)
        with open(datastore_fn, "r") as f:
            data = json.load(f)
            poll = data[str(poll_id)]
        if "responses" not in poll:
            poll["responses"] = {}
        participant_name = request.form["participant_name"]
        # from IPython import embed; embed()

        poll["responses"][participant_name] = request.form.to_dict()
        with open(datastore_fn, "w") as f:
            json.dump(data, f, indent=4)

        return ":-) UAA"

    try:
        with open(datastore_fn, "r+") as f:
            data = json.load(f)

            item = data[str(poll_id)]
    except (json.decoder.JSONDecodeError, builtins.FileNotFoundError, KeyError):
        render_template("error.html")

    return render_template("participant.html", item=item)


@app.route("/results/<int:poll_id>", methods=["GET", "POST"])
def results(poll_id):
    with open(datastore_fn, "r") as f:
        data = json.load(f)

    poll = data[str(poll_id)]

    if request.method == "POST":
        print(request.form)
        print(poll)

    return render_template("results.html", poll=poll)
