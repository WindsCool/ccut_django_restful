import tkinter as tk
from tkinter import *
import tkinter.messagebox


class Base(object):
    def __init__(self):
        self.window = tk.Tk()
        self.menubar = Menu(self.window)
        self.fmenu1 = Menu(self.window)
        self.fmenu1.add_command(label='作者', command = self.author)
        self.menubar.add_cascade(label="关于", menu=self.fmenu1)
        self.window['menu'] = self.menubar

    def author(self):
        tkinter.messagebox.showinfo('作者', '邓琳枫\n20152514\n150408\nversion=1.0.0')

    def destroy(self):
        self.window.destroy()

    def start(self):
        self.window.mainloop()

    def restart(self):
        self.window.destroy()
        self.window.mainloop()
