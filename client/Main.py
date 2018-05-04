import tkinter as tk
from Base import Base


class Main(Base):
    def __init__(self):
        super().__init__()
        self.window.title('CCUT')
        self.window.geometry('600x600')
        self.canvas = tk.Canvas(self.window, bg='black', height=85, width=600)
        self.image_file = tk.PhotoImage(file='welcome.gif')
        image = self.canvas.create_image(125, 0, anchor='nw', image=self.image_file)
        self.canvas.pack()

a = Main()
a.start()

