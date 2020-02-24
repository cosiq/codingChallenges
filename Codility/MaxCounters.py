# Write a function that, given an integer N and a non-empty array A consisting of 
# M integers, returns a sequence of integers representing the values of the counters.
# Result array should be returned as an array of integers.
# For example, given:
# 	A[0] = 3     A[1] = 4     A[2] = 4     A[3] = 6     A[4] = 1     A[5] = 4     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

def maxCounters(N, A):
	cmp = [0] * N
	localMax, globalMax = 0, 0

	for i in range(len(A)):
		if 1 <= A[i] <= N:

			cmp[A[i] - 1] = max(globalMax, cmp[A[i] - 1]) + 1
			localMax = max(localMax, cmp[A[i] - 1])

		if A[i] == N + 1:
			globalMax = localMax

	for i in range(N):
		if cmp[i] < globalMax: cmp[i] = globalMax
   return cmp

# Time: O(N + M)
# Space: O(N)
