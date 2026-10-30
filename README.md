# Iris-Flower-Explorer

A Flask web app for exploring the Iris dataset, with data tables, Matplotlib/Seaborn charts, species pages, and a Flower Finder that identifies a species from its measurements.

## 🌸 Iris Flower Explorer

A Flask web app for exploring the classic Iris flower dataset. Browse the data, view charts, read about each species, and use the Flower Finder to guess a species from its measurements.

## Features

- **Home:** A card for each species (Setosa, Versicolor, Virginica) with a photo.
- **Dataset:** The full data table, filterable by species.
- **Visuals:** 5 charts (bar, scatter, boxplot, histogram, pairplot).
- **Species Pages:** Statistics for each species.
- **Flower Finder:** Enter sepal and petal measurements and the app predicts the species by comparing them to each species' average (Euclidean distance with NumPy).

## Tech Stack

Python · Flask · Pandas · NumPy · Matplotlib · Seaborn · SQLite

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare the data (run once, in this order)

```bash
python data_prep.py
python setup_database.py
python generate_charts.py
```

- `data_prep.py`: Cleans `Iris.csv` and generates `clean_iris.csv` + `summary.json`.
- `setup_database.py`: Builds `iris.db`.
- `generate_charts.py`: Creates the charts in `static/charts/`.

### 3. Run the app

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Project Structure

```text
Iris_Flower_Explorer/
├── app.py                 # Flask routes
├── data_prep.py           # Data cleaning + JSON summary
├── setup_database.py      # Loads clean data into SQLite
├── generate_charts.py     # Matplotlib / Seaborn charts
├── Iris.csv               # Original dataset
├── static/                # CSS, flower images, charts
└── templates/             # HTML pages (Jinja, shared base.html)
```

## Pages

| Route | Description |
|---|---|
| `/` | Home, one card per species |
| `/dataset` | Data table with species filter |
| `/visuals` | Generated charts |
| `/species/<name>` | Stats for one species |
| `/finder` | Predict a species from 4 measurements |
| `/about` | About the project |

## Future Ideas

- A `/compare` page to plot two species side by side.
- Show the 3 closest real rows in the Flower Finder.
- Pagination for the dataset table.

## Dataset

The Iris dataset (R. A. Fisher, 1936): 150 flowers, 3 species, 4 measurements each.
