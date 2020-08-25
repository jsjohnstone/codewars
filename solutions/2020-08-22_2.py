# Printer Errors
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
#
# Examples:
# s="aaabbxbhaijjjm"
# printer_error(s) => "1/14"

def printer_error(s):

    # define some important variables...
    total = len(s)
    i = 0
    err = 0

    # iteration through characters of the string
    while i < total:

        # if one of those characters is not in the allowed list, add an error count
        if s[i] not in "abcdefghijklm":
            err += 1
        i += 1
    
    # format the output as required - num errors / total characters
    result = "{}/{}".format(err, total)
    
    return result
