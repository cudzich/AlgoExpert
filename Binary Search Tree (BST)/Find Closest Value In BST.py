'''

Find Closest Value in Binary Search Tree:
Write a function that takes in a BST and a target integer vale and returns
the closest value to that target value contained in BST.

Assome there will only be one closest value

Each BST node has an integer value, a left and right child node.
A node is said to be valid if and only if it satisfies the BST property:
Its value is strictly greater than the values of every node to its left,
its value is strictly less than or equal to the values of every node to its right.
And its children nodes are either valid BST nodes themselves or None/null.
'''

# Avg.  O(log(n)) T | O(1) S
# Worst O(n) T | O(1) S
class Solution(object):
    def findClosestValueInBst(tree, target):
        return self.findClosestValueInBstHelper(tree, target, float('inf'))
    
    def findClosestValueInBstHelper(tree, target, closest):
        if tree is None:
            return closest
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target > tree.value:
            findClosestValueInBstHelper(tree.right, target, closest)
        elif target < tree.value:
            findClosestValueInBstHelper(tree.left, target, closest)
        else:
            return closest
