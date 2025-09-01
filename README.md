
# ✈️ Flight Booking System

A simple Flight Booking System built using **Python (tkinter / ttkbootstrap)** and **MySQL**.  
It allows users to **search flights, book tickets, and manage bookings**, while **admins can add/manage flights**.

---

## 🚀 Features
- User Login / Signup
- Search flights by **Source** and **Destination**
- Book flights with a single click
- Admin Panel to manage flights
- Modern UI with **ttkbootstrap**
- MySQL Database integration

---

## 🛠️ Tech Stack
- **Frontend/UI**: Python `tkinter` + `ttkbootstrap`
- **Backend**: Python
- **Database**: MySQL
- **Version Control**: GitHub

---

## 📂 Project Structure
```

FlightBookingSystem/
│── flight\_booking.py      # Main Python Application
│── database.sql           # Database schema & sample data
│── README.md              # Project Documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/FlightBookingSystem.git
cd FlightBookingSystem
````

### 2️⃣ Install Requirements

Make sure you have Python installed (>=3.8). Then install dependencies:

```bash
pip install mysql-connector-python ttkbootstrap
```

### 3️⃣ Setup MySQL Database

* Open MySQL and create a database:

```sql
CREATE DATABASE flight_booking;
USE flight_booking;
```

* Run the provided `database.sql` script:

```bash
mysql -u root -p flight_booking < database.sql
```

---

## 🗄️ Database Schema (`database.sql`)

```sql
-- Create Users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Create Flights table
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) UNIQUE NOT NULL,
    source VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    departure_time VARCHAR(50),
    arrival_time VARCHAR(50),
    price DECIMAL(10,2)
);

-- Create Bookings table
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    flight_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

-- Insert sample flights
INSERT INTO flights (flight_number, source, destination, departure_time, arrival_time, price)
VALUES
('AI101', 'Delhi', 'Mumbai', '08:00', '10:00', 4500),
('AI202', 'Mumbai', 'Bangalore', '12:00', '14:30', 5000),
('AI303', 'Chennai', 'Delhi', '16:00', '19:00', 6000);
```

---

## ▶️ Running the Application

```bash
python flight_booking.py
```

---

## 👨‍💻 Admin Access

* Admins can log in with a special account (`username = admin`) to **add/manage flights**.
* Add more features like deleting flights if needed.

---

## 📸 Screenshots

(Add screenshots here after running your project locally)

---

## 📌 Future Improvements

* Add seat selection
* Payment gateway integration
* Flight cancellation & refund system
* Cloud database support (AWS/RDS)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📜 License

This project is licensed under the MIT License.

```

---

👉 This file (`README.md`) includes **everything in one place**:  
- Setup  
- SQL schema  
- Instructions  
- Features  
- Future scope  

Would you like me to also **generate the `database.sql` file separately** so you can just keep it in repo and link it in README?
```
