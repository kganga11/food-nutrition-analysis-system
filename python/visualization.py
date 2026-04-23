import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/velur/Downloads/food_nutrition_project/data/Indian_Food_Nutrition_Processed.csv")

df.columns = [
    "dish_name",
    "calories",
    "carbohydrates",
    "protein",
    "fats",
    "free_sugar",
    "fibre",
    "sodium",
    "calcium",
    "iron",
    "vitamin_c",
    "folate"
]

numeric_cols = [
    "calories", "carbohydrates", "protein", "fats", "free_sugar",
    "fibre", "sodium", "calcium", "iron", "vitamin_c", "folate"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# 1. Histogram of calories
plt.figure(figsize=(8, 5))
plt.hist(df["calories"], bins=30, edgecolor="black")
plt.title("Distribution of Calories")
plt.xlabel("Calories")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 2. Scatter plot: Carbs vs Calories
plt.figure(figsize=(8, 5))
plt.scatter(df["carbohydrates"], df["calories"])
plt.title("Carbohydrates vs Calories")
plt.xlabel("Carbohydrates (g)")
plt.ylabel("Calories (kcal)")
plt.tight_layout()
plt.show()

# 3. Top 10 protein-rich dishes
top10 = df.sort_values("protein", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(top10["dish_name"], top10["protein"])
plt.title("Top 10 Protein-Rich Dishes")
plt.xlabel("Dish Name")
plt.ylabel("Protein (g)")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()