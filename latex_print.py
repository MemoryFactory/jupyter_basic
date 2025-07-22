from sympy import *
from IPython.display import Math,display

def get_raw_repr(s):
    '''Remove qoute of the string'''
    return repr(s).encode('utf-8').decode('unicode-escape')[1:-1]

def lprint(math):
    '''To display math formula of latex type'''
    output = get_raw_repr(latex(math))
    display(Math(output))

def tl(ex):
    '''Print a title'''
    print(f'\n*** {ex} ***')

