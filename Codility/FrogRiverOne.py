# Write a function that, given a non-empty array A consisting of N integers
 # and integer X, returns the earliest time when the frog can jump 
 # to the other side of the river.
# If the frog is never able to jump to the other side of the river, 
# the function should return −1.
# For example, given X = 5 and array A such that
# A[0] = 1   A[1] = 3   A[2] = 1   A[3] = 4   A[4] = 2   A[5] = 3   A[6] = 5   A[7] = 4
# the function should return 6, as explained above.

def FrogRiver(X, A):
	target = (X * (X + 1)) // 2
	cmp, s = set(), 0
	for idx, x in enumerate(A):
		if x not in cmp:
			cmp.add(x)
			s += x
		if s == target: return idx
	return -1

# Time: O(N)
# Space: O(X)

