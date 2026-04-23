pip install pandas scikit-learn matplotlib joblib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import math

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("data/Indian_Food_Nutrition_Processed.csv")

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
# 2. Clean data
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

# -----------------------------
# 3. Features and target
# -----------------------------
X = df[["carbohydrates", "protein", "fats", "free_sugar", "fibre"]]
y = df["calories"]

# -----------------------------
# 4. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 5. Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42, n_estimators=100)
}

best_model = None
best_r2 = -999

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = math.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"\n{name}")
    print("MAE :", round(mae, 3))
    print("RMSE:", round(rmse, 3))
    print("R2  :", round(r2, 3))

    if r2 > best_r2:
        best_r2 = r2
        best_model = model

# -----------------------------
# 6. Save best model
# -----------------------------
joblib.dump(best_model, "best_calorie_model.pkl")
print("\nBest model saved as best_calorie_model.pkl")