# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    	 Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes 
# is represented by the number of edges between them.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root: TreeNode):
	diameter = 0

	def helper(root):
		nonlocal diameter
		if not root: return 0
		left, right = helper(root.left), helper(root.right)
		diameter = max(diameter, left + right)
		return max(left, right) + 1

	helper(root)
	return diameter

# Time: O(N)
# Space: O(N)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.diameter = 0
        self.helper(root)
        return self.diameter
    
    def helper(self, node):
        if not node: return 0
        left, right = self.helper(node.left), self.helper(node.right)
        if left + right + 1 > self.diameter: self.diameter = left + right
        return max(left, right) + 1

# Time: O(N)
# Space: O(N)
