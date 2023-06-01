import tkinter as tk
from tkinter import ttk

def Delete(self):
    title = tk.Label(self.window, text="Eliminación de Usuario", 
                         bg="white", fg="black", font=("Arial", 20))
    title.pack(fill=tk.X)
    title.place(x=0, y=0, width=1000, height=50)

    self.DeleteU = tk.Frame(self.window, bg="white")
    self.DeleteU.pack(fill=tk.BOTH, expand=True)
    self.DeleteU.place(x=0, y=50, width=1000, height=500)

    columns = ("APELLIDOS Y NOMBRES", "C.I.", "SEXO", "TELÉFONO", "ESTADO CIVIL", 
                "FECHA DE NACIMIENTO", "LUGAR DE NACIMIENTO")
    table = ttk.Treeview(self.DeleteU, 
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

    def deleteSelected():
        selected = table.focus()
        values = table.item(selected, 'values')
        self.dataConnection.deleteUser(values[1])
        table.delete(selected)

    deleteButton = tk.Button(self.DeleteU, text="Eliminar",
                            bg="red", fg="white", font=("Arial", 15),
                            command=deleteSelected)
    deleteButton.place(x=900, y=450, width=100, height=50)