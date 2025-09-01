# ✈️ Airline Reservation System  

This project is a basic **Airline Reservation System** built using **Python (Tkinter)** for the user interface and **MySQL** as the database.  

It allows users to sign up, log in, search for flights, book tickets, view and cancel their bookings. Admin users can add or remove flights.  

---

## 🚀 Features  

### User Features  
- 📝 User registration and login  
- 🔎 Search available flights by source and destination  
- 🎟️ Book flights and view personal bookings  
- ❌ Cancel existing bookings  

### Admin Features  
- ➕ Add new flights  
- ➖ Remove flights from the system  

---

## 🛠️ Technologies Used  
- **Python 3**  
- **Tkinter / ttkbootstrap** (for GUI)  
- **MySQL** (for database)  

---

## ⚙️ Setup Instructions  

### 1. Install required Python libraries  
```bash
pip install mysql-connector-python
pip install ttkbootstrap


2. Create the database in MySQL
CREATE DATABASE airline_reservation;
USE airline_reservation;

3. Create the required tables
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(50) NOT NULL,
    source VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    flight_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

4. Update MySQL credentials

In the Python file, edit the database connection function:

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",            # your MySQL username
        password="yourpassword",# your MySQL password
        database="airline_reservation"
    )

5. Run the application
python main.py

👨‍✈️ Default Admin

To log in as Admin, create a user with the username admin.

The system will automatically detect this account as admin.

📂 Project Structure
📦 Airline-Reservation-System
 ┣ 📜 main.py
 ┣ 📜 airline_reservation.sql
 ┣ 📜 README.md
 ┗ 📂 assets   (optional, for icons/images)


✅ You are now ready to run the Airline Reservation System.
