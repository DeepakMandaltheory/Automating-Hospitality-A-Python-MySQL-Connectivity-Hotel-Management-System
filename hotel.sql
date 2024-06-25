-- View all Existing Databases
Show databases;
-- Creating Database named as 'hotel' 
CREATE DATABASE hotel;
use hotel;
   
# Create TABLE FOR Customer Data
CREATE TABLE custdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id INT AUTO_INCREMENT PRIMARY KEY,
    custname VARCHAR(255) NOT NULL,
    addr VARCHAR(255) NOT NULL,
    indate DATE NOT NULL,
    outdate DATE NOT NULL
);
# Create TABLE FOR Room Type
CREATE TABLE roomtype (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_type VARCHAR(255) NOT NULL,
    rate INT NOT NULL
);
# Create TABLE FOR Restaurant 
CREATE TABLE restaurant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    price INT NOT NULL
);
# Create TABLE FOR LAUNDARY
CREATE TABLE laundry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(255) NOT NULL,
    rate INT NOT NULL
);

-- VIew all the tables 
show tables;
-- Insert data into custdata table
INSERT INTO custdata (custname, addr, indate, outdate) VALUES 
('Deepak', 'Mumbai', '2024-06-24', '2024-06-30'),
('Sunny', 'Goa', '2024-06-24', '2024-06-30');

-- Insert data into roomtype table
INSERT INTO roomtype (room_type, rate) VALUES 
('Type A', 1000),
('Type B', 2000),
('Type C', 3000),
('Type D', 4000);

-- Insert data into restaurant table
INSERT INTO restaurant (item_name, price) VALUES 
('tea', 10),
('coffee', 10),
('colddrink', 20),
('samosa', 10),
('sandwich', 50),
('dhokla', 30),
('kachori', 10),
('milk', 20),
('noodles', 50),
('pasta', 50);
INSERT INTO restaurant (item_name, price) VALUES ('Vada pav',20);

-- Insert data into laundary table
INSERT INTO laundry (item, rate) VALUES 
('shirt', 10),
('trousers', 10),
('jacket', 20),
('bed sheet', 15);
select * from custdata;
