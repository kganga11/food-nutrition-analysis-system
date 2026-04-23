-- High protein foods
SELECT dish_name, protein
FROM nutrition_summary
ORDER BY protein DESC
LIMIT 10;

-- Low calorie foods
SELECT dish_name, calories
FROM nutrition_summary
ORDER BY calories ASC
LIMIT 10;