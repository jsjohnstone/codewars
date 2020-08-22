# Convert string to camel case
#
# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
#
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples:
#
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


def to_camel_case(text):
    
    # maintain the case of the first character
    text = text[:1] + text[1:].lower()
    
    #obtain string length and set index
    stlen = len(text)
    i = 0
    
    # iterate through each letter, check if it's a delimiter, and - if 
    # so - remove the delimiter and uppercase the next character
    while i < stlen:
        if text[i] == "_" or text[i] == "-":
            text = text[:i] + text[i + 1:i + 2].upper() + text[i + 2:]
            stlen = stlen - 1
        
        i += 1
        
    return text