import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from user import User
import re

class UserCRUDGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("User CRUD")
        self.create_tabs()
        self.load_users()

    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)

        # Create tabs
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)

        tab_control.add(tab1, text="Add User")
        tab_control.add(tab2, text="Search Users")

        tab_control.pack(expand=True, fill=tk.BOTH)

        # Add User tab
        self.create_add_user_form(tab1)

        # Search Users tab
        self.create_search_users_tab(tab2)

    def create_add_user_form(self, tab):
        # Add User form elements
        name_label = ttk.Label(tab, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(tab)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        ci_label = ttk.Label(tab, text="C.I.:")
        ci_label.grid(row=1, column=0, padx=10, pady=10)
        self.ci_entry = ttk.Entry(tab)
        self.ci_entry.grid(row=1, column=1, padx=10, pady=10)

        gender_label = ttk.Label(tab, text="Gender:")
        gender_label.grid(row=2, column=0, padx=10, pady=10)
        self.gender_entry = ttk.Entry(tab)
        self.gender_entry.grid(row=2, column=1, padx=10, pady=10)

        phone_label = ttk.Label(tab, text="Phone:")
        phone_label.grid(row=3, column=0, padx=10, pady=10)
        self.phone_entry = ttk.Entry(tab)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10)

        civil_status_label = ttk.Label(tab, text="Civil Status:")
        civil_status_label.grid(row=4, column=0, padx=10, pady=10)
        self.civil_status_entry = ttk.Entry(tab)
        self.civil_status_entry.grid(row=4, column=1, padx=10, pady=10)

        birth_date_label = ttk.Label(tab, text="Birth Date:")
        birth_date_label.grid(row=5, column=0, padx=10, pady=10)
        self.birth_date_entry = ttk.Entry(tab)
        self.birth_date_entry.grid(row=5, column=1, padx=10, pady=10)

        address_label = ttk.Label(tab, text="Address:")
        address_label.grid(row=6, column=0, padx=10, pady=10)
        self.address_entry = ttk.Entry(tab)
        self.address_entry.grid(row=6, column=1, padx=10, pady=10)

        add_button = ttk.Button(tab, text="Add User", command=self.add_user)
        add_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_user(self):
        name = self.name_entry.get()
        ci = self.ci_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        civil_status = self.civil_status_entry.get()
        birth_date = self.birth_date_entry.get()
        address = self.address_entry.get()

        # Validate the data here before creating the User object
        if not self.validate_user_name(name):
            return False
        if not self.validate_user_ci(ci):
            return False
        if not self.validate_user_gender(gender):
            return False
        if not self.validate_user_phone(phone):
            return False
        if not self.validate_user_civil_status(civil_status):
            return False
        if not self.validate_user_birth_date(birth_date):
            return False
        if not self.validate_user_address(address):
            return False

        # Create a User object
        user = User(name, ci, gender, phone, civil_status, birth_date, address)

        # Save the user to the CSV file
        self.save_user(user)

        # Clear the form fields
        self.name_entry.delete(0, tk.END)
        # Clear other form fields

        # Reload the user list
        self.load_users()

    def validate_user_name(self, name):
        if name == "":
            tk.messagebox.showerror("Error", "Name is required")
            return False
        if len(name) < 3:
            tk.messagebox.showerror("Error", "Name must be at least 3 characters long")
            return False
        
        if not re.match("^[a-zA-Z ]+$", name):
            tk.messagebox.showerror("Error", "Name must only contain letters")
            return False

        return True
    
    def validate_user_ci(self, ci):
        if ci == "":
            tk.messagebox.showerror("Error", "C.I. is required")
            return False
        
        if not isinstance(ci, str) or len(ci) != 10:
            tk.messagebox.showerror("Error", "C.I. must be a string of 10 characters")
            return False

        province_code = ci[:2]
        if not province_code.isdigit() or not (1 <= int(province_code) <= 24):
            tk.messagebox.showerror("Error", "C.I. is invalid")
            return False

        third_digit = ci[2]
        if not third_digit.isdigit() or not (0 <= int(third_digit) <= 6):
            tk.messagebox.showerror("Error", "C.I. is invalid")
            return False

        try:
            validator = 0
            for i, digit in enumerate(ci):
                value = int(digit)
                if i % 2 == 0:
                    value *= 2
                    if value > 9:
                        value -= 9
                validator += value

            if not validator % 10 == 0:
                tk.messagebox.showerror("Error", "C.I. is invalid")
                return False
        except ValueError:
            tk.messagebox.showerror("Error", "C.I. is invalid")
            return False

        return True
    
    def validate_user_gender(self, gender):
        if gender == '':
            tk.messagebox.showerror("Error", "Gender is required")
            return False
        
        if gender != 'M' or gender != 'F':
            return False
        
        return True

    def validate_user_phone(self, phone):
        if phone == '':
            tk.messagebox.showerror("Error", "Phone is required")
            return False
        
        if not isinstance(phone, str) or len(phone) != 10:
            tk.messagebox.showerror("Error", "Phone must have 10 digits")
            return False
        
        if not phone.isdigit():
            tk.messagebox.showerror("Error", "Phone must only contain numbers")
            return False
        
        return True

    def validate_user_civil_status(self, civil_status):
        if civil_status == '':
            tk.messagebox.showerror("Error", "Civil Status is required")
            return False
        
        if civil_status != 'S' or civil_status != 'M' or civil_status != 'D' or civil_status != 'W':  # noqa: E501
            return False
        
        return True

    def validate_user_birth_date(self, birth_date):
        if birth_date == '':
            tk.messagebox.showerror("Error", "Birth Date is required")
            return False
        
        if not isinstance(birth_date, str):
            tk.messagebox.showerror("Error", "Birth Date error")
            return False
        
        try:
            datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        except ValueError:
            tk.messagebox.showerror("Error", "Birth Date error")
            return False
        
        return True

    def validate_user_address(self, address):
        if address == '':
            tk.messagebox.showerror("Error", "Address is required")
            return False
        
        if not isinstance(address, str):
            tk.messagebox.showerror("Error", "Address error")
            return False
        
        return True
    

    def create_search_users_tab(self, tab):
        # Search Users table
        columns = ('Name','C.I.','Gender','Phone','Civil Status','Birth Date','Address')
        self.users_table = ttk.Treeview(tab, height=15, columns=columns, show="headings")

        for heading in columns:
            self.users_table.heading(heading, text=heading.title())
            self.users_table.column(heading, width=80, stretch=False)

        self.users_table.pack(padx=10, pady=10)

        # Filter options
        filter_frame = ttk.Frame(tab)
        filter_frame.pack(padx=10, pady=10)

        filter_label = ttk.Label(filter_frame, text="Filter by:")
        filter_label.grid(row=0, column=0, padx=5)

        self.filter_entry = ttk.Entry(filter_frame)
        self.filter_entry.grid(row=0, column=1, padx=5)

        filter_button = ttk.Button(filter_frame, text="Filter", command=self.filter_users)
        filter_button.grid(row=0, column=2, padx=5)

        # Load all users initially
        self.load_users()

    def load_users(self):
        # Clear existing data in the table
        self.users_table.delete(*self.users_table.get_children())

        # Read users from the CSV file and populate the table
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User(
                    row["name"],
                    row["ci"],
                    row["gender"],
                    row["phone"],
                    row["civil_status"],
                    row["birth_date"],
                    row["address"]
                )
                self.users_table.insert("", "end", values=(
                     user.name, 
                     user.ci,
                     user.gender, 
                     user.phone, 
                     user.civil_status, 
                     user.birth_date, 
                     user.address))

    def save_user(self, user):
        # Append the user data to the CSV file
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                user.name,
                user.ci,
                user.gender,
                user.phone,
                user.civil_status,
                user.birth_date,
                user.address
            ])

    def filter_users(self):
        keyword = self.filter_entry.get().lower()

        # Clear existing data in the table
        self.users_table.delete(*self.users_table.get_children())

        # Read users from the CSV file and populate the table based on the filter
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if keyword in row["name"].lower() or keyword in row["ci"].lower() or keyword in row["gender"].lower() or keyword in row["phone"].lower() or keyword in row["civil_status"].lower() or keyword in row["birth_date"].lower() or keyword in row["address"].lower():  # noqa: E501
                    user = User(
                        row["name"],
                        row["ci"],
                        row["gender"],
                        row["phone"],
                        row["civil_status"],
                        row["birth_date"],
                        row["address"]
                    )
                    self.users_table.insert("", "end", values=(
                         user.name,
                         user.ci,
                         user.gender,
                         user.phone,
                         user.civil_status,
                         user.birth_date,
                         user.address))

def run_gui():
    root = tk.Tk()
    UserCRUDGUI(root)
    root.mainloop()
