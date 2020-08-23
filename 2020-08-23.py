# Where my anagrams at?
# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/
#
# Examples:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    
    #define an empty list
    anagrams = []
    
    #sort the characters in the given word into alphabetical order
    word_sorted = "". join(sorted(word))
    
    #iterate through potential candidate words given
    for candidate in words:
        #sort the candidate word and see if it matches word_sorted
        if  word_sorted == "". join(sorted(candidate)):
            # if so, append the actual candidate word to anagrams list
            anagrams.append(candidate)
    
    #return the list
    return anagrams