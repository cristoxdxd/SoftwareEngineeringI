import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(current_dir, "GUI")
sys.path.append(database_path)

from mainWindow import Window  # noqa: E402

if __name__ == '__main__':
    Window('Sistema de Gestión de Usuarios', 1000, 600, (True, True))