# Write a function that, given an array A consisting of N integers 
# fulfilling the above conditions, returns the value of the unpaired element.
# For example, given array A such that:
# A[0] = 9  A[1] = 3  A[2] = 9   A[3] = 3  A[4] = 9  A[5] = 7   A[6] = 9
# the function should return 7, as explained in the example above.

def oddOccurrencesXOR(A):
	cmp = 0
	for item in A: cmp ^= item
	return cmp

# Time: O(N)
# Space: O(1)

def oddOccurrences(A):
	cmp = {a: 0 for a in set(A)}
	for i in range(len(A)):
		cmp[A[i]] += 1
	for k, v in cmp.items():
		if v % 2: return k

# Time: O(N)
# Space: O(N)


print(oddOccurrences([9, 3, 9, 3, 9, 7, 9])) # 7