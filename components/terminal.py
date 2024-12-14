import tkinter as tk
from tkinter import scrolledtext

class Terminal:
    def __init__(self, root) -> None:
        '''
        Parameters:
        root widget of application
        '''
        # terminal for execution
        self.terminal = scrolledtext.ScrolledText(root, wrap='word')
        self.terminal.pack(side='bottom', fill='x')

    def clear(self) -> None:
        '''
        This function clears the terminal
        '''
        self.terminal.delete('1.0', tk.END)

    def insert(self, text) -> None:
        '''
        This function inserts text into the terminal

        Parameters:
        text: text to be inserted

        Returns:
        None
        '''
        self.clear()
        self.terminal.insert('1.0', text)