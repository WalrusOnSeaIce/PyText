## About
PyText is a simple text editor for writing scripts in Python. It is useful when you wish to execute Python scripts without saving them as a file. It can be used to create and edit files.

## Development Strategy
* The UI layer is written in components.py file. Each component of the window can be worked on individually. All the classes in the file have the root window as their parent frame.
* The functionality of the app is provide by functions defined in utils.py.
* The main.py organises the components and is the main file of the program.