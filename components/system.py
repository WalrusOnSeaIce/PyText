import tkinter as tk
import components.editor
import utils
import components.terminal
import components.window

class System:
    '''
    The file tab and run/new file command
    '''
    def __init__(self, root):
        self.map = {} # map storing IDs and their corresponding frames
        self.active = None # active window, or the window being displayed
        self.root = root
        self.file_tab = tk.Frame(root, background='white')
        self.file_tab.pack(side='top', fill='x')

        self.run = tk.Button(self.file_tab, text = '|>', foreground = 'green', command = None)
        self.run.pack(side = 'right')
        tk.Button(self.file_tab, text = '+', foreground = 'green', command = lambda: self.new(1 if bool(self.map) == False else max(self.map)+1)).pack(side='right')


    def new(self, name: int):
        window = components.window.Window()
        file_option = tk.Frame(self.file_tab)
        file_option.pack(side='left')
        win_name = tk.Button(file_option, text=str(name), border = 0, command = lambda: self.go_to(name))
        win_name.grid(column=0, row=0)
        close_button = tk.Button(file_option, text='x', foreground='red', command=lambda: self.close(name))
        close_button.grid(column=1, row=0)
        self.map[name] = (window, file_option)
        self.go_to(name)


    def output(self, name: int):
        '''
        This function prints the output to the terminal

        Parameters: terminal object
        '''
        self.map[name][0].terminal.insert(utils.execute(self.map[name][0].editor.editor.get('1.0', 'end-1c')))
        
    def go_to(self, name: int):
        '''
        This function opens the file/window passed as argument

        Parameter: Name of Window
        '''
        self.run['command'] = lambda: self.output(name)
        if self.active != None:
            self.active.hide()
            self.active = self.map[name][0] 
        else:
            self.active = self.map[name][0]
        self.map[name][0].display()


    def close(self, name: int):
        '''
        The function closes the window with a particular name passed as argument.

        name: Name of window
        '''
        if self.map.get(name) is not None:
            self.map[name][0].window.destroy()
            self.map[name][1].destroy()
            del self.map[name]
            if bool(self.map) == True:
                self.go_to(min(self.map))
            else:
                self.run['command'] = None
                

