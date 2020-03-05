# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.
# Example:
	# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7		return its depth = 3.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root: TreeNode):
	return max(maxDepth(root.left), maxDepth(root.right)) + 1 if root else 0

# Time: O(N)
# Space: O(1)

def dfsMaxDepth(root: TreeNode):
	stack, res = [(root, 1)], 0
	while stack:
		node, level = stack.pop()
		if not node.left and not node.right:
			res = max(level, res)
		if node.left: stack.append((node.left, level + 1))
		if node.right: stack.append((node.right, level + 1))
	return res

# Time: O(N)
# Space: O(N)

def dfsMaxDepth(root: TreeNode):
	if not root: return 0
	left, right = dfsMaxDepth(root.left), dfsMaxDepth(root.right)
	return max(left, right) + 1

# Time: O(N)
# Space: O(1)
