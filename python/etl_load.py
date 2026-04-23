pip install pandas mysql-connector-python



import pandas as pd
import mysql.connector

# -----------------------------
# 1. Read dataset
# -----------------------------
file_path = "data/Indian_Food_Nutrition_Processed.csv"
df = pd.read_csv(file_path)

# -----------------------------
# 2. Clean column names
# -----------------------------
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

# -----------------------------
# 3. Basic cleaning
# -----------------------------
df["dish_name"] = df["dish_name"].astype(str).str.strip()
df = df.drop_duplicates(subset=["dish_name"])

numeric_cols = [
    "calories", "carbohydrates", "protein", "fats", "free_sugar",
    "fibre", "sodium", "calcium", "iron", "vitamin_c", "folate"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(0)

# Optional: remove negative values
for col in numeric_cols:
    df[col] = df[col].apply(lambda x: x if x >= 0 else 0)

print("Cleaned rows:", len(df))

# -----------------------------
# 4. Connect to MySQL
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="food_nutrition_db"
)

cursor = conn.cursor()

# -----------------------------
# 5. Insert dishes
# -----------------------------
dish_insert_query = """
INSERT IGNORE INTO dish (dish_name)
VALUES (%s)
"""

for _, row in df.iterrows():
    cursor.execute(dish_insert_query, (row["dish_name"],))

conn.commit()

# -----------------------------
# 6. Get nutrient IDs
# -----------------------------
cursor.execute("SELECT nutrient_id, nutrient_name FROM nutrient")
nutrient_map = {name: nid for nid, name in cursor.fetchall()}

# -----------------------------
# 7. Insert dish_nutrient values
# -----------------------------
dish_nutrient_insert_query = """
INSERT INTO dish_nutrient (dish_id, nutrient_id, amount)
VALUES (%s, %s, %s)
ON DUPLICATE KEY UPDATE amount = VALUES(amount)
"""

nutrient_columns = {
    "Calories": "calories",
    "Carbohydrates": "carbohydrates",
    "Protein": "protein",
    "Fats": "fats",
    "Free Sugar": "free_sugar",
    "Fibre": "fibre",
    "Sodium": "sodium",
    "Calcium": "calcium",
    "Iron": "iron",
    "Vitamin C": "vitamin_c",
    "Folate": "folate"
}

for _, row in df.iterrows():
    cursor.execute("SELECT dish_id FROM dish WHERE dish_name = %s", (row["dish_name"],))
    result = cursor.fetchone()
    if not result:
        continue
    dish_id = result[0]

    for nutrient_name, col_name in nutrient_columns.items():
        nutrient_id = nutrient_map[nutrient_name]
        amount = float(row[col_name])
        cursor.execute(dish_nutrient_insert_query, (dish_id, nutrient_id, amount))

conn.commit()
cursor.close()
conn.close()

print("ETL completed successfully.")