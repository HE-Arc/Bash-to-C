
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
