# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
# adding up all the values along the path equals the given sum.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1 return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recHasPathSum(root, sum):
    if not root: return False
    if root.val == sum and not (root.left or root.right): return True
    sum -= root.val
    return self.recHasPathSum(root.left, sum) or self.recHasPathSum(root.right, sum)

# Time: O(N)
# Space: O(1)

def iterHasPathSum(root, sum):
	if root is None: return False
    stack = [(root, sum)]
    while stack:
        node, _sum = stack.pop()
        if node.val == _sum and not(node.left or node.right): return True
        if node.left: stack.append((node.left, _sum - node.val))
        if node.right: stack.append((node.right, _sum - node.val))
    return False

# Time: O(N)
# Space: O(N)
