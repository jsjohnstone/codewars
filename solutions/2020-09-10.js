# TV Remote
# https://www.codewars.com/kata/5a5032f4fd56cb958e00007a
#
# Test.assertEquals(tvRemote("does"), 16);
# Test.assertEquals(tvRemote("your"), 23);
# Test.assertEquals(tvRemote("solution"), 33);
# Test.assertEquals(tvRemote("work"), 20);
# Test.assertEquals(tvRemote("for"), 12);
# Test.assertEquals(tvRemote("these"), 27);
# Test.assertEquals(tvRemote("words"), 25);

var tvRemote = function(word) {

  // define remote array
  // define current pointer position = 0,0
  // define variables that holds the total
  let remoteArray = [
    ["a","b","c","d","e","1","2","3"],
    ["f","g","h","i","j","4","5","6"],
    ["k","l","m","n","o","7","8","9"],
    ["p","q","r","s","t",".","@","0"],
    ["u","v","w","x","y","z","_","/"]
    ]
  
  let pointerPos = 'a'
  let totalMoves = 0
  
  // getCharacterPosition(character) - return an array (x,y)
  function getCharacterPosition(character) {
    let x
    let y
    
    for(x = 0; x < remoteArray.length; x++) {
      y = remoteArray[x].findIndex(ychar => ychar == character)
      if(y >= 0) { break }
    }
    
    return [x,y]
  }
  
  // distance between two characters - distanceLetters(start,end)
  function distanceLetters(startChar, newChar){
    let a
    let b
    a = getCharacterPosition(startChar)
    b = getCharacterPosition(newChar)
    let x = Math.abs(a[0]-b[0])
    let y = Math.abs(a[1]-b[1])
    return x+y+1
  }
  
  let wordArray = word.split("")
    
  for(i = 0; i < wordArray.length; i++){
    totalMoves = distanceLetters(pointerPos,wordArray[i]) + totalMoves
    pointerPos = wordArray[i]
  }
    
  return totalMoves
  
}
