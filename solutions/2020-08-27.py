# Stop gninnipS My sdroW!
# https://www.codewars.com/kata/5264d2b162488dc400000001/
#
#
# test.assert_equals(spin_words("Welcome"), "emocleW")
# test.assert_equals(spin_words("to"), "to")
# test.assert_equals(spin_words("CodeWars"), "sraWedoC")
# test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
# test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")

def spin_words(sentence):
    # split sentence into words
    split = sentence.split(' ')
    # get the count of words
    wordcount = len(split)
    
    # setup some variables...
    i = 0
    result = ""
    
    # iterate through the word list
    for word in split:
        
        #if the word is more than 5 characters, reverse it!
        if len(word) >= 5:
            word = word[::-1]
        
        #count up for each word
        i += 1
        
        # if there are more words to come, add a space to the end of the sentence
        if i < wordcount:
            result = result + word + " "
        else:
            # or if not, it's the last word, so don't add a space
            result = result + word
            
    # return the sentence!
    return result