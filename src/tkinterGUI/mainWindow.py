import tkinter as tk
from tkinter import ttk
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(current_dir, "..", "database")
sys.path.append(database_path)

from connection import Connection

class Window:
    def __init__(self, title, width, height, resizable):
        self.dataConnection = Connection("cristoxdxd_ci")
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(width=resizable[0], height=resizable[1])

        self.frameUser = None

        self.draw()

    def draw(self):
        title = tk.Label(self.window, text="Sistema de Gestión de Usuarios", bg="white", fg="black", font=("Arial", 20))
        title.pack(fill=tk.X)
        title.place(x=0, y=0, width=800, height=50)

        self.frameUser = tk.Frame(self.window, bg="white")
        self.frameUser.pack(fill=tk.BOTH, expand=True)
        self.frameUser.place(x=0, y=50, width=800, height=550)

        columns = ("APELLIDOS Y NOMBRES", "C.I.", "SEXO", "TELÉFONO", "ESTADO CIVIL", 
                   "FECHA DE NACIMIENTO", "LUGAR DE NACIMIENTO")
        table = ttk.Treeview(self.frameUser, 
                             columns=columns, 
                             show="headings", 
                             height=10)
        table.place(x=0, y=0, width=800, height=550)

        for heading in columns:
            table.heading(heading, text=heading)
            table.column(heading, width=100)

        def fillUsers():
            users = self.dataConnection.getUsersData()
            for user in users:
                table.insert('', 'end', values=user)

        buttonFill = tk.Button(self.frameUser, text="Llenar", command=fillUsers)
        buttonFill.place(x=50, y=100, width=100, height=50)

        self.window.mainloop()

window = Window('Sistema de Gestión de Usuarios', 800, 600, (True, True))