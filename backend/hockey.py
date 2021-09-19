from flask import Flask, render_template, request, abort
import json, random, string

app = Flask(__name__)

TEAMS = ["meerkats", "elephants", "antelopes", "seals", "seagulls", "starfish", "deer", "rabbits", "squirrels",
         "flamingos", "salamanders", "cranes"]


@app.route("/")
def root_page():
    return render_template("base.html")


@app.route("/teams", methods=["GET"])
def teams():
    return json.dumps(TEAMS)


@app.route("/teams/<team_name>", methods=["GET"])
def single_get(team_name=None):
    if team_name not in TEAMS:
        abort(404)

    players = []

    random.seed(team_name)

    # Generates D
    for i in range(6):
        d = {
            "name": "".join(random.choice(string.ascii_letters) for x in range(random.randint(4, 8))),
            "position": "D",
            "goals": random.randint(0, 100),
            "assists": random.randint(0, 100)
        }

        players.append(d)

    # Generates LW
    for i in range(3):
        d = {
            "name": "".join(random.choice(string.ascii_letters) for x in range(random.randint(4, 8))),
            "position": "LW",
            "goals": random.randint(0, 100),
            "assists": random.randint(0, 100)
        }

        players.append(d)

    # Generates RW
    for i in range(3):
        d = {
            "name": "".join(random.choice(string.ascii_letters) for x in range(random.randint(4, 8))),
            "position": "RW",
            "goals": random.randint(0, 100),
            "assists": random.randint(0, 100)
        }

        players.append(d)

    # Generates C
    for i in range(3):
        d = {
            "name": "".join(random.choice(string.ascii_letters) for x in range(random.randint(4, 8))),
            "position": "C",
            "goals": random.randint(0, 100),
            "assists": random.randint(0, 100)
        }

        players.append(d)

    return json.dumps(players)


if __name__ == "__main__":
    app.run()
