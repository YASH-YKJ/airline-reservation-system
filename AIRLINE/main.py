import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# ---------------- CONNECT TO MYSQL ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="vup9cmdkax",  # your MySQL password
        database="airline_reservation"
    )

# ---------------- MAIN APP ----------------
class AirlineReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Reservation System")
        self.root.geometry("950x650")

        self.user_id = None
        self.is_admin = False

        self.login_page()

    # ---------------- LOGIN PAGE ----------------
    def login_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Login", font=("Arial", 22, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Signup", command=self.signup_page).pack()

    def login(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                       (self.username_entry.get(), self.password_entry.get()))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.user_id = user[0]
            # check if admin
            self.is_admin = True if self.username_entry.get() == "admin" else False
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    # ---------------- SIGNUP PAGE ----------------
    def signup_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Signup", font=("Arial", 22, "bold")).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        self.new_username = tk.Entry(self.root)
        self.new_username.pack()

        tk.Label(self.root, text="Email:").pack()
        self.new_email = tk.Entry(self.root)
        self.new_email.pack()

        tk.Label(self.root, text="Password:").pack()
        self.new_password = tk.Entry(self.root, show="*")
        self.new_password.pack()

        tk.Button(self.root, text="Register", command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.login_page).pack()

    def register_user(self):
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s,%s,%s)",
                           (self.new_username.get(), self.new_email.get(), self.new_password.get()))
            conn.commit()
            messagebox.showinfo("Success", "User registered successfully!")
            self.login_page()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")
        conn.close()

    # ---------------- DASHBOARD ----------------
    def dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Dashboard", font=("Arial", 22, "bold")).pack(pady=20)

        if self.is_admin:
            tk.Button(self.root, text="Add Flight", command=self.add_flight_page, width=20).pack(pady=10)
            tk.Button(self.root, text="Remove Flight", command=self.remove_flight_page, width=20).pack(pady=10)
        else:
            tk.Button(self.root, text="Search Flights", command=self.search_flights_page, width=20).pack(pady=10)
            tk.Button(self.root, text="My Bookings", command=self.my_bookings_page, width=20).pack(pady=10)

        tk.Button(self.root, text="Logout", command=self.login_page, width=20).pack(pady=10)

    # ---------------- SEARCH FLIGHTS ----------------
    def search_flights_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Search Flights", font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(self.root, text="Source:").pack()
        self.src_entry = tk.Entry(self.root)
        self.src_entry.pack()

        tk.Label(self.root, text="Destination:").pack()
        self.dest_entry = tk.Entry(self.root)
        self.dest_entry.pack()

        tk.Button(self.root, text="Search", command=self.search_flights).pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Flight", "Source", "Destination", "Departure", "Arrival", "Price"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True)

        tk.Button(self.root, text="Book Selected Flight", command=self.book_flight).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.dashboard).pack()

    def search_flights(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flights WHERE source=%s AND destination=%s",
                       (self.src_entry.get(), self.dest_entry.get()))
        flights = cursor.fetchall()
        conn.close()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for flight in flights:
            self.tree.insert("", "end", values=(
                flight[1], flight[2], flight[3], flight[4], flight[5], flight[6]
            ))

    def book_flight(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Select a flight first")
            return

        flight_number = self.tree.item(selected)["values"][0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT flight_id FROM flights WHERE flight_number=%s", (flight_number,))
        flight_id = cursor.fetchone()[0]

        cursor.execute("INSERT INTO bookings (user_id, flight_id) VALUES (%s, %s)", (self.user_id, flight_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Flight booked successfully!")

    # ---------------- MY BOOKINGS ----------------
    def my_bookings_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="My Bookings", font=("Arial", 20, "bold")).pack(pady=20)

        self.book_tree = ttk.Treeview(self.root, columns=("Flight", "Source", "Destination", "Departure", "Arrival", "Price"), show="headings")
        for col in self.book_tree["columns"]:
            self.book_tree.heading(col, text=col)
        self.book_tree.pack(fill="both", expand=True)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT b.booking_id, f.flight_number, f.source, f.destination, f.departure_time, f.arrival_time, f.price
            FROM bookings b
            JOIN flights f ON b.flight_id = f.flight_id
            WHERE b.user_id=%s
        """, (self.user_id,))
        bookings = cursor.fetchall()
        conn.close()

        for book in bookings:
            self.book_tree.insert("", "end", iid=book[0], values=book[1:])

        tk.Button(self.root, text="Cancel Selected Booking", command=self.cancel_booking).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.dashboard).pack(pady=10)

    def cancel_booking(self):
        selected = self.book_tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Select a booking first")
            return

        booking_id = selected

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM bookings WHERE booking_id=%s", (booking_id,))
        conn.commit()
        conn.close()

        self.book_tree.delete(booking_id)
        messagebox.showinfo("Success", "Booking cancelled successfully!")

    # ---------------- ADMIN: ADD FLIGHT ----------------
    def add_flight_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Flight", font=("Arial", 20, "bold")).pack(pady=20)

        labels = ["Flight Number", "Source", "Destination", "Departure (YYYY-MM-DD HH:MM:SS)", "Arrival (YYYY-MM-DD HH:MM:SS)", "Price"]
        self.entries = {}
        for lbl in labels:
            tk.Label(self.root, text=lbl).pack()
            self.entries[lbl] = tk.Entry(self.root)
            self.entries[lbl].pack()

        tk.Button(self.root, text="Add Flight", command=self.add_flight).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.dashboard).pack()

    def add_flight(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO flights (flight_number, source, destination, departure_time, arrival_time, price)
                          VALUES (%s,%s,%s,%s,%s,%s)""",
                       (self.entries["Flight Number"].get(),
                        self.entries["Source"].get(),
                        self.entries["Destination"].get(),
                        self.entries["Departure (YYYY-MM-DD HH:MM:SS)"].get(),
                        self.entries["Arrival (YYYY-MM-DD HH:MM:SS)"].get(),
                        self.entries["Price"].get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Flight added successfully!")

    # ---------------- ADMIN: REMOVE FLIGHT ----------------
    def remove_flight_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Remove Flight", font=("Arial", 20, "bold")).pack(pady=20)

        self.rem_tree = ttk.Treeview(self.root, columns=("Flight", "Source", "Destination", "Departure", "Arrival", "Price"), show="headings")
        for col in self.rem_tree["columns"]:
            self.rem_tree.heading(col, text=col)
        self.rem_tree.pack(fill="both", expand=True)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flights")
        flights = cursor.fetchall()
        conn.close()

        for f in flights:
            self.rem_tree.insert("", "end", iid=f[0], values=f[1:])

        tk.Button(self.root, text="Delete Selected Flight", command=self.remove_flight).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.dashboard).pack()

    def remove_flight(self):
        selected = self.rem_tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Select a flight first")
            return

        flight_id = selected
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM flights WHERE flight_id=%s", (flight_id,))
        conn.commit()
        conn.close()

        self.rem_tree.delete(flight_id)
        messagebox.showinfo("Success", "Flight removed successfully!")


# ---------------- RUN APP ----------------
root = tk.Tk()
app = AirlineReservationApp(root)
root.mainloop()
