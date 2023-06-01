import re
from tkinter import messagebox
import datetime

def validate_user_name(name):
        if name == "":
            messagebox.showerror("Error", "Nombre requerido")
            return False
        
        name_words = name.split(" ")
        if len(name_words) < 3:
            messagebox.showerror("Error", "Nombres y Apellidos requeridos")
            return False #
        
        if not re.match("^[a-zA-Z ]+$", name):
            messagebox.showerror("Error", "El nombre solo puede contener letras y espacios")
            return False

        return True
    
def validate_user_ci(ci):
    if ci == "":
        messagebox.showerror("Error", "C.I. requerida")
        return False
    
    if not isinstance(ci, str) or len(ci) != 10:
        messagebox.showerror("Error", "C.I. tiene 10 dígitos")
        return False

    province_code = ci[:2]
    if not province_code.isdigit() or not (1 <= int(province_code) <= 24):
        messagebox.showerror("Error", "C.I. inválida")
        return False

    third_digit = ci[2]
    if not third_digit.isdigit() or not (0 <= int(third_digit) <= 6):
        messagebox.showerror("Error", "C.I. inválida")
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
            messagebox.showerror("Error", "C.I. inválida")
            return False
    except ValueError:
        messagebox.showerror("Error", "C.I. inválida")
        return False

    return True

def validate_user_gender(gender):
    if gender == '':
        messagebox.showerror("Error", "Sexo requerido")
        return False
    
    return True

def validate_user_phone(phone):
    if phone == '':
        messagebox.showerror("Error", "Telefono requerido")
        return False
    
    if not isinstance(phone, str) or len(phone) != 10:
        messagebox.showerror("Error", "Teléfono tiene 10 dígitos")
        return False
    
    if not phone.isdigit():
        messagebox.showerror("Error", "El teléfono solo puede contener números")
        return False
    
    return True

def validate_user_civil_status(civil_status):
    if civil_status == '':
        messagebox.showerror("Error", "Estado Civil requerido")
        return False
    
    return True

def validate_user_birth_date(birth_date):
    if birth_date == '':
        messagebox.showerror("Error", "Fecha de Nacimiento requerida")
        return False
    
    try:
        datetime.datetime.strptime(birth_date, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Error", "Error en formato de fecha")
        return False
    
    # TODO: Validate age

    if datetime.datetime.strptime(birth_date, '%Y-%m-%d') > datetime.datetime.now():
        messagebox.showerror("Error", "Fecha de nacimiento inválida")
        return False
    
    return True

def validate_user_birth_place(address):
    if address == '':
        messagebox.showerror("Error", "Lugar de nacimiento requerido")
        return False
    
    if not isinstance(address, str):
        messagebox.showerror("Error", "Error en lugar de nacimiento")
        return False
    
    return True
