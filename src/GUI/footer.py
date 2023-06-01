import tkinter as tk

from newUsers import Create
from readUsers import Read
# from updateUsers import Update
# from deleteUsers import Delete

def Footer(self):
    buttonCreate = tk.Button(self.window, text="Nuevo",
                             command=lambda: self.showFrame(Create(self)),
                             bg="white", fg="black", font=("Arial", 15))
    buttonCreate.place(x=10, y=550, width=100, height=50)
    buttonRead = tk.Button(self.window, text="Leer", 
                           command=lambda: self.showFrame(Read(self)),
                           bg="white", fg="black", font=("Arial", 15))
    buttonRead.place(x=110, y=550, width=100, height=50)
    # buttonUpdate = tk.Button(self.window, text="Actualizar", 
    #                          command=lambda: self.showFrame(Update(self)),
    #                          bg="white", fg="black", font=("Arial", 15))
    # buttonUpdate.place(x=210, y=550, width=100, height=50)
    # buttonDelete = tk.Button(self.window, text="Eliminar", 
    #                          command=lambda: self.showFrame(Delete(self)),
    #                          bg="white", fg="black", font=("Arial", 15))
    # buttonDelete.place(x=310, y=550, width=100, height=50)
    buttonExit = tk.Button(self.window, text="Salir",
                           command=self.window.destroy,
                           bg="red", fg="white", font=("Arial", 15))
    buttonExit.place(x=500, y=550, width=100, height=50)
