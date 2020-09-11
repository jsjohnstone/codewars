//Big Party
//https://www.codewars.com/kata/59c4b77163b362cf5a000004
//
// Test.assertEquals(maxNumberOfPeopleAtTheParty([[3,9],[2,5],[6,8],[2,6]]),3)
// Test.assertEquals(maxNumberOfPeopleAtTheParty([[1,100],[1,100]]),2)
// Test.assertEquals(maxNumberOfPeopleAtTheParty([[1,50],[51,100]]),1)
// Test.assertEquals(maxNumberOfPeopleAtTheParty([[1,50],[50,100]]),2)
// Test.assertEquals(maxNumberOfPeopleAtTheParty([[1,10000],[10001,10002]]),1)

function maxNumberOfPeopleAtTheParty(records){
  
  // instantiate totalrecords object, with nothing
  let totalRecord = { 0: 0 }
  
  // get records
  // for the records array, loop through the elements 
  records.forEach(element => {
    for(i = element[0]; i <= element[1]; i++) {
      (i in totalRecord) ? totalRecord[i]++ : totalRecord[i] = 1
    }
  })
  
  // find the key with the greatest value and return it.
  let max_min = 0
  let max_value = 0
  
  Object.keys(totalRecord).forEach(key => {
    if(totalRecord[key] > max_value) { 
      max_min = key 
      max_value = totalRecord[key]
    }
  });
  
  return max_value
  
}
