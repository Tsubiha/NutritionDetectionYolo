CREATE DATABASE Fruit_Detection;
USE Fruit_Detection;

-- Creating the FruitData table
CREATE TABLE FruitData (
    dataset_Id INT NOT NULL,
    Fruit_Name VARCHAR(20) NOT NULL,
    Color VARCHAR(20) NOT NULL,
    Fruit_image VARCHAR(20) NOT NULL,
    PRIMARY KEY (dataset_Id)
);

-- Creating the Nutrition_info table
CREATE TABLE Nutrition_info (
    Fruit_name VARCHAR(20) NOT NULL,
    Proteins_level VARCHAR(10) NOT NULL,
    Carbo_level VARCHAR(10) NOT NULL,
    Fats_level VARCHAR(10) NOT NULL,
    Fiber_level VARCHAR(10) NOT NULL,
    Vit_level VARCHAR(10) NOT NULL,
    Nutrition_description VARCHAR(50) NOT NULL,
    PRIMARY KEY (Fruit_name),
);

-- Inserting sample data into FruitData table
INSERT INTO FruitData (dataset_Id, Fruit_Name, Color, Fruit_image) VALUES
(1, 'Apple', 'Red', 'apple.jpg'),
(2, 'Banana', 'Yellow', 'banana.jpg'),
(3, 'Orange', 'Orange', 'orange.jpg'),
(4, 'Grapes', 'Purple', 'grapes.jpg'),
(5, 'Mango', 'Yellow', 'mango.jpg'),
(6, 'Strawberry', 'Red', 'strawberry.jpg'),
(7, 'Blueberry', 'Blue', 'blueberry.jpg'),
(8, 'Pineapple', 'Brown', 'pineapple.jpg'),
(9, 'Watermelon', 'Green', 'watermelon.jpg'),
(10, 'Peach', 'Pink', 'peach.jpg');

-- Inserting sample data into Nutrition_info table
INSERT INTO Nutrition_info (Fruit_name, Proteins_level, Carbo_level, Fats_level, Fiber_level, Vit_level, Nutrition_description) VALUES
('Apple', '0.3g', '14g', '0.2g', '2.4g', 'Vitamin C', 'Rich in fiber and Vitamin C'),
('Banana', '1.3g', '27g', '0.3g', '3.1g', 'Vitamin B6', 'Good source of Vitamin B6 and fiber'),
('Orange', '0.9g', '12g', '0.1g', '2.4g', 'Vitamin C', 'Excellent source of Vitamin C'),
('Grapes', '0.6g', '18g', '0.2g', '0.9g', 'Vitamin K', 'Rich in antioxidants and Vitamin K'),
('Mango', '0.8g', '15g', '0.4g', '1.6g', 'Vitamin A', 'High in Vitamin A and C'),
('Strawberry', '0.8g', '8g', '0.4g', '2g', 'Vitamin C', 'High in Vitamin C and antioxidants'),
('Blueberry', '0.7g', '14g', '0.3g', '2.4g', 'Vitamin C', 'High in Vitamin C and fiber'),
('Pineapple', '0.5g', '13g', '0.1g', '1.4g', 'Vitamin C', 'Good source of Vitamin C and manganese'),
('Watermelon', '0.6g', '8g', '0.2g', '0.4g', 'Vitamin A', 'Hydrating and rich in Vitamin A and C'),
('Peach', '1g', '10g', '0.3g', '1.5g', 'Vitamin C', 'Rich in vitamins and antioxidants');

SELECT * from [dbo].[FruitData]

select * from [dbo].[Nutrition_info]