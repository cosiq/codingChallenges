# Given a binary tree, return all root-to-leaf paths.
# Example:
#	 Input:
#    1
#  /   \
# 2     3
#  \
#   5
#	 Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recBinaryTreePath(root):
	if not root: return []
	if not (root.left or root.right): return [str(root.val)]
	return ([str(root.val) + "->" + item for item in recBinaryTreePath(root.left)]
	 + [str(root.val) + "->" + jtem for jtem in recBinaryTreePath(root.right)])

# Time: O(N)
# Space: O(N)

def BinaryTreePath(root):
    if not root: return []
    res, stack = [], [(root, "")]
    while stack:
        node, lst = stack.pop()
        if not (node.left or node.right): res.append(lst + str(node.val))
        if node.left: stack.append((node.left, lst + str(node.val) + "->"))
        if node.right: stack.append((node.right, lst + str(node.val) + "->"))
    return res

# Time: O(N)
# Space: O(N)
