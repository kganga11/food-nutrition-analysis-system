CREATE DATABASE food_nutrition_db;
USE food_nutrition_db;

CREATE TABLE dish (
    dish_id INT AUTO_INCREMENT PRIMARY KEY,
    dish_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE nutrient (
    nutrient_id INT AUTO_INCREMENT PRIMARY KEY,
    nutrient_name VARCHAR(100) NOT NULL UNIQUE,
    unit VARCHAR(20) NOT NULL
);

CREATE TABLE dish_nutrient (
    dish_id INT NOT NULL,
    nutrient_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (dish_id, nutrient_id),
    FOREIGN KEY (dish_id) REFERENCES dish(dish_id),
    FOREIGN KEY (nutrient_id) REFERENCES nutrient(nutrient_id)
);