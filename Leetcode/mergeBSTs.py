# Given two binary trees and imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. 
# The merge rule is that if two nodes overlap, then sum node values up 
# as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
	if not t1: return t2
	if not t2: return t1
	# setting the root node
	root = TreeNode(t1.val + t2.val)
	root.left = mergeTrees(t1.left, t2.left)
	root.right = mergeTrees(t1.right, t2.right)
	return root

# 		1
#     /   \
#    3     2
#   /
#  5
ex1 = TreeNode(1)
ex1.left = TreeNode(3)
ex1.left.left = TreeNode(5)
ex1.right = TreeNode(2)

# 		2
#     /   \
#    1     3
#     \     \
#      4     7
ex2 = TreeNode(2)
ex2.left = TreeNode(1)
ex2.right = TreeNode(3)
ex2.left.right = TreeNode(4)
ex2.right.right = TreeNode(7)

# 		3
#     /   \
#    4     5
#   / \     \
#  5   4     7
res = mergeTrees(ex1, ex2)
print(res.val) # 3
print(res.left.val) # 4
print(res.right.val) # 5
print(res.left.left.val) # 5
print(res.left.right.val) # 4
print(res.right.right.val) # 7
