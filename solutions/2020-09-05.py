# Detect Pangram
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
#
# pangram = "The quick brown fox jumps over the lazy dog."
# Test.assert_equals(is_pangram(pangram), True)
# not_pangram1 = "This isn't a pangram!"
# Test.assert_equals(is_pangram(not_pangram1), False, not_pangram1 + " is not a pangram.")

import string

def is_pangram(s):
    abc = list('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    
    for char in abc:
        if s.find(char) == -1:
            return False
    return True