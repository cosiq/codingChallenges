# Write a function that, given an array A, returns 1 
# if array A is a permutation and 0 if it is not.
# For example, given array A such that:
# 	A[0] = 4     A[1] = 1     A[2] = 3     A[3] = 2
# the function should return 1.

def permCheck(A):
	lenLst, lenSet = len(A), len(set(A))
	if lenLst != lenSet: return 0
	return 1 if max(A) == lenSet else 0

# Time: O(N)
# Space: O(1)