# Bit Counting
# https://www.codewars.com/kata/526571aae218b8ee490006f4/
#
# Count bits in the binary version of a number
# e.g. bin(4) = "100" which contas 1 "1"
#
# test.assert_equals(count_bits(0), 0)
# test.assert_equals(count_bits(4), 1)
# test.assert_equals(count_bits(7), 3)
# test.assert_equals(count_bits(9), 2)
# test.assert_equals(count_bits(10), 2)

def count_bits(n):
    # set counter to 0
    count = 0
    
    # convert number to list of binary characters
    binlist = list("{0:b}".format(n))
    
    # iterate through list, add each character (will be 1 or 0)
    for char in binlist: count += int(char)
        
    # return sum of 1s
    return count