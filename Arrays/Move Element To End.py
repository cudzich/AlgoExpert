'''

Given an array of integers and a target value. Move all target value's
in array to the end.


Two pointers, sliding window algorithm
--------------------------------------
i will traverse the array from beginning
j will traverse the array from the end (len(num) -1)
while i and j don't overlap, check if value at j is equal to target,
if value at target is equal to j, decrement j, break to while
We check if i and j overlap, if not then we now know that the value at
j can be swapped with i if i is equal to target.
Complete the swap if i is equal to target, move the window (i++),
if i is not equal to target, increment i.

when i and j overlap, return array

'''

class Solution(object):
    def moveElementToEnd(self, num, target):
        i = 0
        j = len(num) - 1
        while i < j:
            #print(str(num[i])+' : '+str(num[j]))
            if num[j] == target:
                j -= 1
                continue
            elif num[i] == target:
                #tmp = num[j]
                #num[j] = num[i]
                #num[i] = tmp
                num[i], num[j] = num[j], num[i]
                i += 1
            else:
                i += 1

        return num

obj = Solution()
test = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
r = obj.moveElementToEnd(test, 5)
print(r)
