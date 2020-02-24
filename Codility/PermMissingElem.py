# Write a function that, given an array A, returns the value of the missing element.
# For example, given array A such that: A[0] = 2   A[1] = 3   A[2] = 1   A[3] = 5
# the function should return 4, as it is the missing element.

def permMissing(A):
	if len(A) == 0: return 1
	if max(A) == len(A): return max(A) + 1
	A = sorted(A)
	for i in range(1, len(A) + 1):
		if A[i - 1] != i: return i

# Time: O(N)
# Space: O(N)

def simplePermMissing(A):
	n = len(A) + 1
	return (n * (n + 1)) // 2 - sum(A)

# Time: O(N)
# Space: O(1)

def xorPermMissing(A):
	n = len(A) + 1
	item = n
	for i in range(1, n):
		item ^= A[i - 1]
		item ^= i
	return item

# Time: O(N)
# Space: O(1)

