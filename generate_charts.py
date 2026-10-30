"""
Step 4: Generate the Charts
------------------------------
Uses Matplotlib + Seaborn (Data Visualization lecture) to create the
images shown on the Visualizations page. Charts are saved as .png
files inside static/charts/ so Flask can serve them directly.

Run once, AFTER data_prep.py:
    python generate_charts.py
"""
import matplotlib
matplotlib.use("Agg")  # no GUI needed, just save to file
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("clean_iris.csv")
sns.set_style("whitegrid")

# 1) Bar chart -> average petal length per species
plt.figure(figsize=(6, 4))
avg_petal = df.groupby("Species")["PetalLengthCm"].mean()
plt.bar(avg_petal.index, avg_petal.values, color="#4682b4")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("static/charts/bar_petal_length.png")
plt.close()

# 2) Scatter plot -> sepal length vs petal length, colored by species
plt.figure(figsize=(6, 4))
sns.scatterplot(
    data=df, x="SepalLengthCm", y="PetalLengthCm",
    hue="Species", palette="Set2"
)
plt.title("Sepal Length vs Petal Length")
plt.tight_layout()
plt.savefig("static/charts/scatter_sepal_petal.png")
plt.close()

# 3) Boxplot -> petal width distribution per species
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Species", y="PetalWidthCm", hue="Species", palette="Set3", legend=False)
plt.title("Petal Width Distribution per Species")
plt.tight_layout()
plt.savefig("static/charts/box_petal_width.png")
plt.close()

# 4) Histogram -> sepal width distribution (whole dataset)
plt.figure(figsize=(6, 4))
plt.hist(df["SepalWidthCm"], bins=15, color="#6f42c1", edgecolor="white")
plt.title("Sepal Width Distribution (All Flowers)")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("static/charts/hist_sepal_width.png")
plt.close()

# 5) Pairplot -> relationship between every pair of features
pair = sns.pairplot(df, hue="Species", palette="Set2", corner=True)
pair.savefig("static/charts/pairplot.png")

print("All charts saved inside static/charts/")
