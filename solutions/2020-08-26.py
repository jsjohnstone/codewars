# Find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836/
#
# Example tests:
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
# test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
# test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
# test.assert_equals(find_it([10]), 10);
# test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
# test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);

def find_it(seq):
    # convert list into set to remove duplicates
    unique = set(seq)
    
    # iterate through the set
    for char in unique:
        # count occurences of each set item, try divide by 2 - if a remainder occurs, it's an odd number
        if (seq.count(char) % 2) is not 0:
            
            # ... so return that set item!
            return char
        
    return None
