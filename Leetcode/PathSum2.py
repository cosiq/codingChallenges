# Given a binary tree and a sum, find all root-to-leaf paths 
# where each path's sum equals the given sum.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1			Return: [[5,4,11,2], [5,8,4,5]]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recPathSum():
	if not root: return []
    if sum == root.val and not (root.left or root.right): return [[root.val]]
    cmp = self.recPathSum(root.left, sum - root.val) + self.recPathSum(root.right, sum - root.val)
    return [[root.val] + item for item in cmp]

# Time: O(N)
# Space: O(N)

def dfsPathSum(root, sum): 
    if not root: return []
    res = []
    stack = [(root, sum - root.val, [root.val])]
    while stack:
        curr, _sum, lst = stack.pop()
        if _sum == 0 and not (curr.left or curr.right): res.append(lst)
        if curr.right: stack.append((curr.right, _sum - curr.right.val, lst + [curr.right.val]))
        if curr.left: stack.append((curr.left, _sum - curr.left.val, lst + [curr.left.val]))
    return res 

# Time: O(N)
# Space: O(N)

def bfsPathSum(root, sum):
	if not root: return []
    res = []
    queue = [(root, root.val, [root.val])]
    while queue:
        curr, _sum, lst = queue.pop(0)
        if _sum == sum and not (curr.left or curr.right): res.append(lst)
        if curr.left: queue.append((curr.left, _sum + curr.left.val, lst + [curr.left.val]))
        if curr.right: queue.append((curr.right, _sum + curr.right.val, lst + [curr.right.val]))
    return res

# Time: O(N)
# Space: O(N)

