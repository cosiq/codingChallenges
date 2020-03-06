# Given a binary tree, check whether it is a mirror of itself 
# (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recSymmetricTree(root: TreeNode):
	if not root: return True
	def helper(t1, t2):
		if not t1 and not t2: return True
		if not t1 or not t2: return False
		return (t1.val == t2.val) and helper(t1.left, t2.right) and helper(t1.right, t2.left)
	return helper(root.left, root.right)		

# Time: O(N)
# Space: O(N)

def iterSymmetricTree(root: TreeNode):
	if not root: return True
    stack = []
    stack.append([root.left, root.right])
    while stack:
        t1, t2 = stack.pop()
        if not t1 and not t2: continue
        if (not t1 or not t2) or t1.val != t2.val: return False
        stack.append([t1.left, t2.right])
        stack.append([t1.right, t2.left])
    return True
            
# Time: O(N)
# Space: O(N)
