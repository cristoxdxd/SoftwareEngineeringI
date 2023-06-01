import tkinter as tk
from tkinter import messagebox

from footer import Footer
from readUsers import Read

def Login(self):
    title = tk.Label(self.window, text="DB Usuarios", 
                         bg="white", fg="black", font=("Arial", 20),
                         justify=tk.CENTER)
    title.pack(fill=tk.X)
    title.place(x=0, y=0, width=1000, height=50)

    self.Login = tk.Frame(self.window, bg="white")
    self.Login.pack(fill=tk.X)
    self.Login.place(x=0, y=50, width=1000, height=550)

    self.Login.title = tk.Label(self.Login, text="Login",
                                bg="white", fg="black", font=("Arial", 20))
    self.Login.title.pack(fill=tk.X)
    self.Login.title.place(x=250, y=0, width=500, height=50)

    self.Login.username = tk.Label(self.Login, text="Username",
                                   bg="white", fg="black", font=("Arial", 15))
    self.Login.username.pack(fill=tk.X)
    self.Login.username.place(x=250, y=50, width=500, height=50)

    self.Login.usernameEntry = tk.Entry(self.Login, bg="white", fg="black", 
                                        font=("Arial", 15),
                                        justify=tk.CENTER)
    self.Login.usernameEntry.pack(fill=tk.X)
    self.Login.usernameEntry.place(x=350, y=100, width=300, height=50)

    self.Login.password = tk.Label(self.Login, text="Password",
                                        bg="white", fg="black", font=("Arial", 15))
    self.Login.password.pack(fill=tk.X)
    self.Login.password.place(x=250, y=150, width=500, height=50)

    self.Login.passwordEntry = tk.Entry(self.Login, bg="white", fg="black", 
                                        font=("Arial", 15), show="*",
                                        justify=tk.CENTER)
    self.Login.passwordEntry.pack(fill=tk.X)
    self.Login.passwordEntry.place(x=350, y=200, width=300, height=50)

    self.Login.loginButton = tk.Button(self.Login, text="Login", bg="white", fg="black", 
                                       font=("Arial", 15),
                                       command=lambda:[Read(self), Footer(self)] if self.Login.usernameEntry.get() == "admin" and self.Login.passwordEntry.get() == "admin" else messagebox.ERROR('Error', 'Usuario no válido'))  # noqa: E501
    self.Login.loginButton.pack(fill=tk.X)
    self.Login.loginButton.place(x=400, y=275, width=200, height=50)
