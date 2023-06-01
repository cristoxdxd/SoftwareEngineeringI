import tkinter as tk
from tkinter import ttk
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(current_dir, "..", "database")
sys.path.append(database_path)

from connection import Connection  # noqa: E402

def Update(self):
    title = tk.Label(self.window, text="Actualización de Usuario", 
                         bg="white", fg="black", font=("Arial", 20))
    title.pack(fill=tk.X)
    title.place(x=0, y=0, width=1000, height=50)

    self.UpdateU = tk.Frame(self.window, bg="white")
    self.UpdateU.pack(fill=tk.BOTH, expand=True)
    self.UpdateU.place(x=0, y=50, width=1000, height=500)

    userWantedLabel = tk.Label(self.UpdateU, text="Usuario a Actualizar",
                               bg="white", fg="black", font=("Arial", 15))
    userWantedLabel.pack(fill=tk.X)
    userWantedLabel.place(x=0, y=0, width=300, height=50)

    userWantedEntry = ttk.Entry(self.UpdateU, font=("Arial", 15))
    userWantedEntry.pack(fill=tk.X)
    userWantedEntry.place(x=310, y=15, width=130, height=25)

    def getUserWanted():
        return Connection.searchUser(self.dataConnection, userWantedEntry.get())

    userWantedButton = tk.Button(self.UpdateU, text="Buscar",
                                 bg="white", fg="black", font=("Arial", 15),
                                 command=lambda: getUserWanted())  
    userWantedButton.pack(fill=tk.X)
    userWantedButton.place(x=450, y=15, width=150, height=25)

    labelPhone = tk.Label(self.UpdateU, text="Teléfono", bg="white", font=("Arial", 15),
                          anchor="e", justify=tk.RIGHT)
    labelPhone.place(x=50, y=200, width=150, height=25)
    entryPhone = tk.Entry(self.UpdateU, font=("Arial", 15),
                          )
    entryPhone.place(x=210, y=200, width=200, height=25)

    labelCivilStatus = tk.Label(self.UpdateU, text="Estado Civil", bg="white", 
                                font=("Arial", 15), anchor="e", justify=tk.RIGHT)
    labelCivilStatus.place(x=50, y=250, width=150, height=50)
    listCivilStatusH = ["SOLTERO", "CASADO", "DIVORCIADO", "VIUDO"]
    listCivilStatusM = ["SOLTERA", "CASADA", "DIVORCIADA", "VIUDA"]
    cmbCivilStatus = tk.ttk.Combobox(self.UpdateU, state="readonly", font=("Arial", 15))
    cmbCivilStatus.place(x=210, y=260, width=200, height=25)

    def updateCivilStatusList(*args):
        if Connection.getUserGender(self, userWantedEntry()) == "HOMBRE":
            cmbCivilStatus.config(values=listCivilStatusH)
        elif Connection.getUserGender(self, userWantedEntry()) == "MUJER":
            cmbCivilStatus.config(values=listCivilStatusM)

    cmbCivilStatus.bind("<<ComboboxSelected>>", updateCivilStatusList)

    buttonUpdate = tk.Button(self.UpdateU, text="Actualizar", bg="white", fg="black",
                             font=("Arial", 15), 
                             command=lambda: Connection.updateUser(self.dataConnection, 
                                                                   entryPhone.get(), 
                                                                   cmbCivilStatus.get(), 
                                                                   userWantedEntry.get()))
    buttonUpdate.place(x=50, y=300, width=150, height=50)
