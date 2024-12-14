'''
This file contains the utility functions for the app, like opening a new file, editing functions etc. These functions should be ideally called in the components.py file
'''
from io import StringIO
import sys

def execute(code):
    '''
    This function takes the code to be executed as an argument and displays in the space beneath the editor

    Parameters:
    code: the code to be executed

    Returns:
    The terminal output
    '''
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code)
    except:
        raise
    finally:
        sys.stdout = old_stdout
    output = redirected_output.getvalue()
    return output

    