# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example:
#	 Input: n = 12
#	 Output: 3 
#	 Explanation: 12 = 4 + 4 + 4.

dp = [0]

def numSquares(n: int):
	lst, length = dp, len(dp)
	for i in range(length, n + 1):
		lst.append(1 + min(lst[i - j * j] for j in range(int(i ** .5), 0, -1)))
	return lst[n]

# Time: O(N ** 2)
# Space: O(N)


numSquares(12) # 3
numSquares(13) # 2

