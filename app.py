from flask import Flask, render_template, request
import sqlite3
import json
import numpy as np

app = Flask(__name__)

DESCRIPTIONS = {
    "setosa": "The smallest of the three species, with short, rounded petals "
              "and a distinctly narrow, delicate build.",
    "versicolor": "A mid-sized Iris with balanced proportions -- petals and "
                  "sepals that sit right between Setosa and Virginica.",
    "virginica": "The largest species, known for its long petals and wide, "
                 "showy sepals.",
}

LATIN_NAMES = {
    "setosa": "Iris setosa",
    "versicolor": "Iris versicolor",
    "virginica": "Iris virginica",
}


# ---------- Helpers ----------

def get_flowers(species_filter=None):
    connection = sqlite3.connect("iris.db")
    connection.row_factory = sqlite3.Row

    if species_filter:
        flowers = connection.execute(
            "SELECT * FROM iris WHERE Species = ?", (species_filter,)
        ).fetchall()
    else:
        flowers = connection.execute("SELECT * FROM iris").fetchall()

    connection.close()
    return flowers


def get_summary():
    with open("summary.json", "r") as f:
        return json.load(f)


# ---------- Routes ----------

@app.route("/")
def home():
    summary = get_summary()
    return render_template(
        "index.html", summary=summary, descriptions=DESCRIPTIONS, active="home"
    )


@app.route("/dataset")
def dataset():
    species_filter = request.args.get("species")
    flowers = get_flowers(species_filter)
    all_species = ["setosa", "versicolor", "virginica"]
    return render_template(
        "dataset.html",
        flowers=flowers,
        all_species=all_species,
        selected=species_filter,
        active="dataset"
    )


@app.route("/visuals")
def visuals():
    return render_template("visuals.html", active="visuals")


@app.route("/species/<name>")
def species_detail(name):
    summary = get_summary()
    stats = summary.get(name)
    return render_template(
        "species.html",
        name=name,
        stats=stats,
        descriptions=DESCRIPTIONS,
        latin_names=LATIN_NAMES,
        active="flowers"
    )


@app.route("/finder", methods=["GET", "POST"])
def finder():
    result = None

    if request.method == "POST":
        # 1) Read the 4 measurements from the form
        user_values = np.array([
            float(request.form["sepal_length"]),
            float(request.form["sepal_width"]),
            float(request.form["petal_length"]),
            float(request.form["petal_width"]),
        ])

        # 2) Compare the user's flower to the average flower of each species
        summary = get_summary()
        best_species = None
        best_distance = None

        for species, stats in summary.items():
            species_avg = np.array([
                stats["avg_sepal_length"],
                stats["avg_sepal_width"],
                stats["avg_petal_length"],
                stats["avg_petal_width"],
            ])
            # Euclidean distance using NumPy
            distance = np.linalg.norm(user_values - species_avg)

            if best_distance is None or distance < best_distance:
                best_distance = distance
                best_species = species

        result = {
            "species": best_species,
            "distance": round(float(best_distance), 3)
        }

    return render_template(
        "finder.html", result=result, descriptions=DESCRIPTIONS, active="finder"
    )


@app.route("/about")
def about():
    return render_template("about.html", active="about")


if __name__ == "__main__":
    app.run(debug=True)
