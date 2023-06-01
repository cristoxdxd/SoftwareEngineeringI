from tkinter import messagebox
import sys
import os

from validateData import *  # noqa: F403

current_dir = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(current_dir, "..", "database")
sys.path.append(database_path)

from connection import Connection  # noqa: E402

def saveData(self, entryName, entryCI, radioSex, 
             entryPhone, cmbCivilStatus, 
             entryBirthDate, entryBirthPlace):                        
            try:
                # Validate
                if not validate_user_name(entryName.get()):  # noqa: F405
                    return
                if not validate_user_ci(entryCI.get()):  # noqa: F405
                    return
                if not validate_user_phone(entryPhone.get()):  # noqa: F405
                    return
                if not validate_user_birth_date(entryBirthDate.get()):  # noqa: F405
                    return
                if not validate_user_birth_place(entryBirthPlace.get()):  # noqa: F405
                    return
                
                # Save
                Connection.addUser(self.dataConnection, entryName.get().upper(), entryCI.get(), 
                                   radioSex.get(), entryPhone.get(), 
                                   cmbCivilStatus.get(), entryBirthDate.get(), 
                                   entryBirthPlace.get().upper())
                messagebox.showinfo('Registro', 'Usuario registrado correctamente')
            except Exception as e:
                messagebox.showerror('Error', str(e))