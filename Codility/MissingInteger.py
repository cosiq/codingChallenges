# Write a function that, given an array A of N integers, 
# returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

def missingElements(A):
	cmp = {}
	for item in A:
		if item not in cmp and item > 0: cmp[item] = 1
	for i in range(1, len(A) + 1):
		if i not in cmp: return i
	return len(A) + 1

# Time: O(N)
# Space: O(N)

def simpleMissingElements(A):
	A, c = set(A), 1
	while c in A:
		c += 1
	return c

# Time: O(N)
# Space: O(N)
