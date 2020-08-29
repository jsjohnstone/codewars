# Valid Parentheses (5 kyu)
# https://www.codewars.com/kata/52774a314c2333f0a7000688/
#
# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)


def valid_parentheses(string):
    
    # set a counter to 0
    t = 0
    
    # iteration through each character in the string
    for char in list(string):
        #if it's a (, add one to track the pair
        if char == "(":
            t += 1
        #if it's a ), remove one to close the tracked pair
        elif char == ")":
            t -= 1
        
        #if at any point we go below 0, we've got brackets in the wrong order
        if t < 0:
            break
    
    # after iteration, if t <> 0, brackets are unbalanced
    if t != 0:
        return False
    else:
    # otherwise, the brackets must be correct!
        return True