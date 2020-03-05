# Invert a binary tree.

# Example:
# 	Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recInvertTree(root: TreeNode):
	if root: root.left, root.right = invertTree(root.right), invertTree(root.left)
	return root

# Time: O(N)
# Space: O(N)

def iterInvertTree(root: TreeNode):
	stack = [root]
	while stack:
		node = stack.pop()
		if node:
			node.right, node.left = node.left, node.right
			stack.extend([node.right, node.left])
	return root

# Time: O(N)
# Space: O(N)
