import tkinter as tk
from tkinter import scrolledtext

class Editor:
    '''
    Includes the file tab, editor widget and the scrolledtext
    '''
    def __init__(self, root) -> None:
        '''
        Parameters:
        root: root widget of the application
        terminal: terminal of the object
        name: name of the file
        '''
        

        # main editor
        self.editor = scrolledtext.ScrolledText(root, wrap='word')
        self.editor.pack(side='top', fill='x')
    
    def clear(self) -> None:
        '''
        This function deletes all text in the editor
        '''
        self.editor.delete('1.0', tk.END)

    def insert(self, text: str) -> None:
        '''
        This function clears the editor and inserts text into it

        Parameters:
        text: The text to be inserted

        Returns:
        None
        '''
        self.clear()
        self.editor.insert('1.0', text)