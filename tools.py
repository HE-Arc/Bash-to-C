
'''
Project: Bash-To-C
Authors: Kim Biloni & Malik Fleury
Python version: 3.6
'''

def is_float(str):
    result = True
    try:
        float(str)
    except:
        result = False
    return result

def is_int(str):
    result = True
    try:
        int(str)
    except:
        result = False
    return result
