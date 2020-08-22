# Printer Errors
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    total = len(s)
    i = 0
    err = 0
    
    while i < total:
        if s[i] not in "abcdefghijklm":
            err += 1
        i += 1
    
    result = "{}/{}".format(err, total)
    
    return result
