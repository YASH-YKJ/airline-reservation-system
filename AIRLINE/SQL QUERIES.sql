-- Create a new database
CREATE DATABASE airline_reservation;
USE airline_reservation;

-- Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Flights Table
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) UNIQUE NOT NULL,
    source VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Bookings Table
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    flight_id INT,
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

-- Insert some sample flights
INSERT INTO flights (flight_number, source, destination, departure_time, arrival_time, price)
VALUES
('AI101', 'Delhi', 'Mumbai', '2025-09-02 09:00:00', '2025-09-02 11:00:00', 4500.00),
('AI102', 'Mumbai', 'Delhi', '2025-09-02 15:00:00', '2025-09-02 17:00:00', 4600.00),
('AI201', 'Delhi', 'Bangalore', '2025-09-03 08:00:00', '2025-09-03 11:30:00', 6000.00),
('AI202', 'Bangalore', 'Delhi', '2025-09-03 14:00:00', '2025-09-03 17:30:00', 6200.00);
