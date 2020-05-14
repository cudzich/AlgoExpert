// O(n) time | O(1) space
function isValidSubsequence(array, sequence) {
  let length = sequence.length;
  let count = 0;
  let sub_element = sequence[count];

   for (var i = 0; i < array.length; i++) {
     if(array[i] == sub_element) {
       count++;
       if( count == length) {
	  return true
	}
      sub_element = sequence[count];
     }
   }
	
  return false;
}
