# Replace with Alphabet Position
# https://www.codewars.com/kata/546f922b54af40e1e90001da/

def alphabet_position(text):
    index = list('abcdefghijklmnopqrstuvwxyz')
    result = []

    for char in list(text.lower()):
        try:
            pos = str(index.index(char) + 1)
            result.append(pos)
        except:
            pass
 
    return ' '.join(result)
