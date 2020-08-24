# Which are in?
# https://www.codewars.com/kata/550554fd08b86f84fe000a58/
#
# Example test:
# a1 = ["live", "arp", "strong"] 
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp', 'live', 'strong']
# test.assert_equals(in_array(a1, a2), r)

def in_array(array1, array2):
    
    #define an empty list
    r = []
    array1_dedup = []
    
    #sort the short array
    array1.sort()
    
    #deduplicate array1
    for i in array1:
        if i not in array1_dedup:
            array1_dedup.append(i)
    
    #iterate through the short array
    for short in array1_dedup:
        #iterate through the long array
        for long in array2:
            #check if the short string exists in the current long string
            if long.find(short) >= 0:
                #if it does, add it to the results list
                r.append(short)
                #...and then break out of the inner loop
                break
                
    #return r (empty list or with matching strings)
    return r