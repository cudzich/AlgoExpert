'''
array = [12,3,1,2,-6,5,-8,6]
target = 0

Given a non-empty distinct array, find triplet elements that sum up to the target
value. Return a 2 dimensional array of the triplets, the numbers within
the triplets should be in ascending order as well as the triplets themselves.

Naive solution: 3 for loops, not optimal
iterate over the array once,
at each element, iterate over the array another time
at each element of the second for loop, iterate over the rest of the array

For example, 12+3+x = 0, etc..
             12+1+x = 0, etc..

Hashmap, store the elements from array in a hashmap.
Complete 2 for loops to calculate the sum. Run into duplicates, etc..


---------------------------------------
Optimal solution: T = O(n^2) | S = O(n)

Sort the array in ascending order [-8,-6,1,2,3,5,6,12]
- Traversing the array from left to right guarantees elements increase
- Traversing the array from right to left guarantees elements decrease
- This can be used to our advantage during the search for our target sum
We can now loop over the array and set up our left and right pointers
- left pointer equals position at current element + 1
- right pointer equals positino at the last element in array
We can now check if element + left + right = Target
- if current sum & target are equal, add to array of results as array
-- we now have to update the pointers, since moving the left pointer increases the sum and
right pointer decreases the sum, we should move both of them. l++, r--
if the current sum is not equal to target, then we need to move our pointers
-if current sum is below target(negative), we need to increase our sum by moving the right pointer
-if current sum is above target(positive), we need to decrease our sum by moving the left pointer
When left and right pointer overlap, we move on to the next element in array. 


'''

def threeNumberSum(array, targetSum):
    # Write your code here.
    if len(array) < 3:
        return []
    
    array.sort()
    result = []
    
    for i in range(len(array) - 2): # 3rd value from end of array
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum > targetSum:    #move right
                right -= 1
            elif currentSum < targetSum: #move left
                left += 1
            else: #currentSum = targetSum
                result.append([array[i], array[left], array[right]])
                right -= 1
                left += 1
    
    return result
