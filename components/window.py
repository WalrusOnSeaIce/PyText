import tkinter as tk
import components.editor
import components.terminal

class Window:
    def __init__(self):
        self.window = tk.Frame()
        self.editor = components.editor.Editor(self.window)
        self.terminal = components.terminal.Terminal(self.window)
        self.window.pack(side='top', fill='x')

    def display(self):
        '''
        This method dispays the window
        '''
        self.window.pack(side='top', fill='x')

    def hide(self):
        self.window.pack_forget()

