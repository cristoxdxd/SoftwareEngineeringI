import tkinter as tk
from tkcalendar import DateEntry

from saveData import saveData

def Create(self):
    title = tk.Label(self.window, text="Registro de Nuevos Usuarios", 
                         bg="white", fg="black", font=("Arial", 20))
    title.pack(fill=tk.X)
    title.place(x=0, y=0, width=1000, height=50)

    self.CreateU = tk.Frame(self.window, bg="white")
    self.CreateU.pack(fill=tk.BOTH, expand=True)
    self.CreateU.place(x=0, y=50, width=1000, height=500)

    labelName = tk.Label(self.CreateU, text="Nombres", bg="white", font=("Arial", 15),
                         anchor="e", justify=tk.RIGHT)
    labelName.place(x=50, y=50, width=150, height=25)
    entryName = tk.Entry(self.CreateU, font=("Arial", 15))
    entryName.place(x=210, y=50, width=300, height=25)

    # Label alignment right
    labelCI = tk.Label(self.CreateU, text="C.I.", bg="white", font=("Arial", 15),
                       anchor="e", justify=tk.RIGHT)
    labelCI.place(x=50, y=100, width=150, height=25)
    entryCI = tk.Entry(self.CreateU, font=("Arial", 15))
    entryCI.place(x=210, y=100, width=200, height=25)

    labelSex = tk.Label(self.CreateU, text="Sexo", bg="white", font=("Arial", 15),
                        anchor="e", justify=tk.RIGHT )
    labelSex.place(x=50, y=150, width=150, height=25)
    radioSex = tk.StringVar()
    radioSex.set("HOMBRE")
    radioSex1 = tk.Radiobutton(self.CreateU, text="HOMBRE", bg="white", 
                               variable=radioSex, value="HOMBRE", font=("Arial", 15))
    radioSex1.place(x=210, y=140, width=120, height=50)
    radioSex2 = tk.Radiobutton(self.CreateU, text="MUJER", bg="white", 
                               variable=radioSex, value="MUJER", font=("Arial", 15))
    radioSex2.place(x=350, y=140, width=100, height=50)

    labelPhone = tk.Label(self.CreateU, text="Teléfono", bg="white", font=("Arial", 15),
                          anchor="e", justify=tk.RIGHT)
    labelPhone.place(x=50, y=200, width=150, height=25)
    entryPhone = tk.Entry(self.CreateU, font=("Arial", 15))
    entryPhone.place(x=210, y=200, width=200, height=25)

    labelCivilStatus = tk.Label(self.CreateU, text="Estado Civil", bg="white", 
                                font=("Arial", 15), anchor="e", justify=tk.RIGHT)
    labelCivilStatus.place(x=50, y=250, width=150, height=50)
    listCivilStatusH = ["SOLTERO", "CASADO", "DIVORCIADO", "VIUDO"]
    listCivilStatusM = ["SOLTERA", "CASADA", "DIVORCIADA", "VIUDA"]
    cmbCivilStatus = tk.ttk.Combobox(self.CreateU, state="readonly", font=("Arial", 15),
                                     values=listCivilStatusH)
    cmbCivilStatus.place(x=210, y=260, width=200, height=25)
    
    def updateCivilStatusList(*args):
        if radioSex.get() == "HOMBRE":
            cmbCivilStatus.config(values=listCivilStatusH)
        elif radioSex.get() == "MUJER":
            cmbCivilStatus.config(values=listCivilStatusM)

    radioSex.trace('w', updateCivilStatusList)

    labelBirthDate = tk.Label(self.CreateU, text="Fecha Nac.", bg="white", 
                              font=("Arial", 15), anchor="e", justify=tk.RIGHT)
    labelBirthDate.place(x=50, y=300, width=150, height=25)

    entryBirthDate = DateEntry(self.CreateU, width=12, background='white',
                               foreground='black', borderwidth=2, year=2020,
                               font=("Arial", 15), locale='es_CO', 
                               date_pattern='YYYY-mm-dd', showweeknumbers=False, 
                               weekendbackground='white', weekendforeground='black')
    entryBirthDate.place(x=210, y=300, width=150, height=27)

    labelBirthPlace = tk.Label(self.CreateU, text="Lugar Nac.", bg="white",
                               font=("Arial", 15), anchor="e", justify=tk.RIGHT)
    labelBirthPlace.place(x=50, y=350, width=150, height=25)
    entryBirthPlace = tk.Entry(self.CreateU, font=("Arial", 15))
    entryBirthPlace.place(x=210, y=350, width=300, height=25)

    buttonCreate = tk.Button(self.CreateU, text="Crear", bg="white", fg="black",
                             font=("Arial", 15),
                             command=lambda: saveData(self, entryName, entryCI, radioSex,
                                              entryPhone, cmbCivilStatus,
                                              entryBirthDate, entryBirthPlace))
    buttonCreate.place(x=700, y=400, width=100, height=50)