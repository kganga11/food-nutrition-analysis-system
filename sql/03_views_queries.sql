USE food_nutrition_db;

-- View for calories, protein, carbs, fats per dish
CREATE OR REPLACE VIEW nutrition_summary AS
SELECT 
    d.dish_id,
    d.dish_name,
    MAX(CASE WHEN n.nutrient_name = 'Calories' THEN dn.amount END) AS calories,
    MAX(CASE WHEN n.nutrient_name = 'Protein' THEN dn.amount END) AS protein,
    MAX(CASE WHEN n.nutrient_name = 'Carbohydrates' THEN dn.amount END) AS carbohydrates,
    MAX(CASE WHEN n.nutrient_name = 'Fats' THEN dn.amount END) AS fats
FROM dish d
JOIN dish_nutrient dn ON d.dish_id = dn.dish_id
JOIN nutrient n ON dn.nutrient_id = n.nutrient_id
GROUP BY d.dish_id, d.dish_name;

