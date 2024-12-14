import tkinter as tk
from components import system

root = tk.Tk()
root.title('PyText')
root.state('zoomed')
root.iconbitmap(None)

system = system.System(root)
system.new(1)

root.mainloop()
