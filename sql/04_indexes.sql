CREATE INDEX idx_dish ON dish(dish_name);
CREATE INDEX idx_nutrient ON nutrient(nutrient_name);
CREATE INDEX idx_dn_dish ON dish_nutrient(dish_id);