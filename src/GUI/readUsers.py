import tkinter as tk
from tkinter import ttk

def Read(self):
    title = tk.Label(self.window, text="DB Usuarios", 
                         bg="white", fg="black", font=("Arial", 20))
    title.pack(fill=tk.X)
    title.place(x=0, y=0, width=1000, height=50)

    self.ReadU = tk.Frame(self.window, bg="white")
    self.ReadU.pack(fill=tk.BOTH, expand=True)
    self.ReadU.place(x=0, y=50, width=1000, height=500)

    columns = ("APELLIDOS Y NOMBRES", "C.I.", "SEXO", "TELÉFONO", "ESTADO CIVIL", 
                "FECHA DE NACIMIENTO", "LUGAR DE NACIMIENTO")
    table = ttk.Treeview(self.ReadU, 
                            columns=columns, 
                            show="headings", 
                            height=10)
    table.place(x=0, y=0, width=900, height=550)

    for heading in columns:
        table.heading(heading, text=heading)
        table.column(heading, width=100)

    def fillUsers():
        users = self.dataConnection.getUsersData()
        for user in users:
            table.insert('', 'end', values=user)

    fillUsers()

    # def updateUsers():
    #     for i in table.get_children():
    #         table.delete(i)
    #     fillUsers()

    # buttonUpdate = tk.Button(self.ReadU, text="Actualizar", command=updateUsers)
    # buttonUpdate.place(x=900, y=450, width=100, height=50)