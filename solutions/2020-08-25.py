# Sum of Digits / Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00/
#
# Examples:
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    
    # obtain length of number (number of digits)
    n_len = len(str(n))
    
    # if number of digits is > 1...
    while n_len > 1:
        
        # convert n into a list of digits (16 becomes [1,6])
        n_list = list(str(n))
        
        # reset n to 0
        n = 0
        
        # for each digit in n_list, add it to n (e.g. n=0 + 1 + 6 = 7)
        for i in n_list:
            n += int(i)
        
        # update the length of the new n (7) before looping around again
        n_len = len(str(n))
     
    # if len(n) = 1, return n
    return n