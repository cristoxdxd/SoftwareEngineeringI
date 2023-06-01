import tkinter as tk
import sys
import os

from footer import Footer
from center import center
from login import Login
from readUsers import Read

current_dir = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(current_dir, "..", "database")
sys.path.append(database_path)

from connection import Connection  # noqa: E402

class Window:
    def __init__(self, title, width, height, resizable):
        self.dataConnection = Connection("cristoxdxd_ci")
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(width=resizable[0], height=resizable[1])
        center(self.window)

        self.frames = {
            'Login': None,
            'CreateU': None,
            'ReadU': None,
            'UpdateU': None,
            'DeleteU': None
        }

        self.draw()

    def showFrame(self, frame_name):
        self.hideFrames()
        frame = self.frames.get(frame_name)
        if frame is not None:
            frame.place(x=0, y=50)
            

    def hideFrames(self):
        for frame in self.frames.values():
            if frame is not None:
                frame.pack_forget()

    def draw(self):
        Login(self)
        # Footer(self)
        # Read(self)

        self.window.mainloop()
