# Write a function that, given an array A consisting of N integers and an integer K, 
# returns the array A rotated K times
# For example, given A = [3, 8, 9, 7, 6] and K = 3
# the function should return [9, 7, 6, 3, 8]
# [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
# [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
# [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

# Assume that 
# 	1. N and K are integers within the range [0..100]
# 	2. each element of array A is an integer within the range [−1,000..1,000].

def cyclicRotation(A, K):
	n = len(A)
	if n == 0: return A
	K %= n
	return A[n-K:] + A[:n-K]


cyclicRotation([3, 8, 9, 7, 6], 3) # [9, 7, 6, 3, 8]

# Time: O(1)
# Space: O(N + K)