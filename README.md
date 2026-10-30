# 🌸 Iris Flower Explorer — Build Steps

A simple Flask project built the same way as the Book Store example, but
using the Iris dataset instead of books. It touches every part of the
course: File Handling, NumPy/Pandas, Matplotlib/Seaborn, and Flask.

## Folder structure

```
Iris_Flower_Explorer/
├── Iris.csv
├── data_prep.py
├── setup_database.py
├── generate_charts.py
├── app.py
├── static/
│   ├── style.css
│   ├── images/         (setosa.jpg, versicolor.jpg, virginica.jpg)
│   └── charts/          (created automatically by generate_charts.py)
└── templates/
    ├── base.html        (shared nav + footer, other pages extend this)
    ├── index.html
    ├── dataset.html
    ├── visuals.html
    ├── species.html
    ├── finder.html
    └── about.html
```

### v2 — Botanical redesign

The site now uses a soft lavender / muted green / cream color palette,
rounded cards with real flower photos, a hero section on the homepage,
tabs on the dataset page, and a result card (with photo) on the Flower
Finder page. All pages share one `base.html` layout so the nav bar and
footer stay consistent everywhere — this is standard Flask/Jinja
template inheritance (`{% extends %}` / `{% block %}`), nothing outside
the course.

## Run order (do this once, in this order)

```bash
pip install flask pandas numpy matplotlib seaborn

python data_prep.py         # cleans Iris.csv -> clean_iris.csv + summary.json
python setup_database.py    # builds iris.db from clean_iris.csv
python generate_charts.py   # builds the 5 PNG charts in static/charts/

python app.py                # starts the site at http://127.0.0.1:5000
```

## What each file does (matches the lecture topics)

- **data_prep.py** — Pandas cleaning (drop duplicates/NaNs, rename species)
  + writes a JSON summary file (File Handling lecture: `json.dump`).
- **setup_database.py** — same pattern as the Book Store's
  `setup_database.py`: pandas `DataFrame.to_sql()` into SQLite.
- **generate_charts.py** — Matplotlib + Seaborn: bar, scatter, boxplot,
  histogram, pairplot, all saved as images (Data Visualization lecture).
- **app.py** — Flask routes, reading from SQLite (`sqlite3`) and from
  the JSON summary file. The `/finder` route uses **NumPy**
  (`np.linalg.norm`) to compute the Euclidean distance between the
  numbers a visitor types in and each species' average flower —
  that's the "creative" feature that ties NumPy into the website.

## Pages

| Route            | What it shows                                             |
|-------------------|-------------------------------------------------------------|
| `/`               | Home — one card per species, links to details               |
| `/dataset`        | Full data table, filterable by species                      |
| `/visuals`        | The 5 generated charts                                      |
| `/species/<name>` | Stats for one species                                       |
| `/finder`         | Form → guesses the species from 4 measurements (NumPy)      |
| `/about`          | Short project description                                   |

## Ideas if you want to extend it later (optional, not required)

- Add a `/compare` page that plots two species side by side.
- Let `/finder` also show the 3 closest actual rows from the dataset,
  not just the species average.
- Add pagination to `/dataset` (150 rows is small, but it's good practice).
