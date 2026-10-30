# Iris-Flower-Explorer
A Flask web app for exploring the Iris dataset, with data tables, Matplotlib/Seaborn charts, species pages, and a Flower Finder that identifies a species from its measurements.




🌸 Iris Flower Explorer

A Flask web app for exploring the classic Iris flower dataset. Browse the data, view charts, read about each species, and use the Flower Finder to guess a species from its measurements.

Features
Home: a card for each species (Setosa, Versicolor, Virginica) with a photo
Dataset: the full data table, filterable by species
Visuals: 5 charts (bar, scatter, boxplot, histogram, pairplot)
Species pages: statistics for each species
Flower Finder: enter sepal and petal measurements and the app predicts the species by comparing them to each species' average (Euclidean distance with NumPy)
Tech stack

Python · Flask · Pandas · NumPy · Matplotlib · Seaborn · SQLite

Getting started
bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Prepare the data (run once, in this order)
python data_prep.py          # cleans Iris.csv -> clean_iris.csv + summary.json
python setup_database.py     # builds iris.db
python generate_charts.py    # creates the charts in static/charts/

# 3. Run the app
python app.py

Then open http://127.0.0.1:5000 in your browser.

Project structure
Iris_Flower_Explorer/
├── app.py                # Flask routes
├── data_prep.py          # data cleaning + JSON summary
├── setup_database.py     # loads clean data into SQLite
├── generate_charts.py    # Matplotlib / Seaborn charts
├── Iris.csv              # original dataset
├── static/               # CSS, flower images, charts
└── templates/            # HTML pages (Jinja, shared base.html)

Pages
Route	Description
/	Home, one card per species
/dataset	Data table with species filter
/visuals	Generated charts
/species/<name>	Stats for one species
/finder	Predict a species from 4 measurements
/about	About the project
Future ideas
A /compare page to plot two species side by side
Show the 3 closest real rows in the Flower Finder
Pagination for the dataset table
Dataset

The Iris dataset (R. A. Fisher, 1936): 150 flowers, 3 species, 4 measurements each.
