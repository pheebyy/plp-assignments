# Task: Analyzing Data with Pandas and Visualizing Results with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ----------------------------------
# Task 1: Load and Explore the Dataset
# ----------------------------------

try:
    # Load Iris dataset directly from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # convert to Pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

    print("✅ Dataset loaded successfully!\n")

    # Display first few rows
    print("🔎 First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Check structure: data types + missing values
    print("📊 Dataset Info:")
    print(df.info(), "\n")

    print("❓ Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (Iris has no missing values, but let's show method)
    df = df.dropna()  # could also use df.fillna(value) if needed

except FileNotFoundError:
    print("⚠️ Error: Dataset file not found!")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

# ----------------------------------
# Task 2: Basic Data Analysis
# ----------------------------------

print("\n📈 Statistical Summary:")
print(df.describe(), "\n")

# Grouping example: average petal length per species
grouped = df.groupby("species")["petal length (cm)"].mean()
print("🌸 Average Petal Length by Species:")
print(grouped, "\n")

# Interesting pattern:
print("💡 Observation: Iris-virginica has the largest average petal length.\n")

# ----------------------------------
# Task 3: Data Visualization
# ----------------------------------

sns.set(style="whitegrid")  # prettier plots

# 1. Line Chart (cumulative petal length across rows, simulating 'trend')
plt.figure(figsize=(8,5))
df["petal length (cm)"].cumsum().plot(kind="line")
plt.title("Cumulative Petal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Petal Length (cm)")
plt.show()

# 2. Bar Chart (avg petal length per species)
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
plt.figure(figsize=(8,5))
plt.hist(df["sepal length (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (sepal length vs petal length)
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

print("✅ All tasks completed successfully!")
