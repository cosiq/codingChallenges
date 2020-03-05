# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example:
#	 Input: n = 12
#	 Output: 3 
#	 Explanation: 12 = 4 + 4 + 4.

def recNumSquares(n: int):
	num = int(n ** .5)
	if num ** 2 == n: return 1
	res = n
	for j in range(1, num + 1):
		res = min(res, recNumSquares(n - j ** 2))
	return res + 1

# Time: O(2 ** N)
# Space: O(1)

def memoNumSquares(n: int):
	memo = {}
	def helper(n: int):
		if n in memo: return memo[n]
		num = int(n ** .5)
		if num ** 2 == n: memo[n] = 1
		else:
			res = n
			for j in range(1, num + 1):
				res = min(res, helper(n - j ** 2))
			memo[n] = res + 1
		return memo[n]
	return helper(n)

# Time: O(N ** 2)
# Space: O(N)

# Runtime Analysis
# http://courses.csail.mit.edu/6.006/fall09/lecture_notes/lecture18.pdf


# n -> a1, a2, ..., ak
# n = a1 + a2 + ... + ak
# n - a1 = a2 + ... + ak   [sub-problem]

# Memoization
# Goal: Find the least number of perfect square numbers of sum n
# 		(min number of perfect squares that sum up to n)
# Base Case: dp[0] = 0
# State: dp[i] = min number of perfect squares that sum up to n
# Recurrence Relation:
# 	State below dp[i] that we care about: dp[i - ak], s.t. ak = j * j (perfect square)
# 	dp[i] = function(dp[i - j * j]) = min(dp[i], dp[i - j * j] + 1)

# 	j * j <= i -> j <= sqrt(i)



dp = [0]
def numSquares(n: int):
	lst = dp
	for i in range(1, n + 1):
		lst.append(1 + min(lst[i - j * j] for j in range(int(i ** .5), 0, -1)))
	return lst[n]

# Time: O(N ** 2)
# Space: O(N)


numSquares(12) # 3
numSquares(13) # 2


# minimum number -> can we model it as a graph -> if then, finding shortest path would be helpful
# How can we determine the edges and how to determine the nodes?
# Nodes: perfect square number <= n
# Find the least number of perfect square numbers that sum up to n

# Finding shortest path from 0 to n 
# s.t. that x, y are connected if their difference is perfect squares

def bfsNumSquares1(n: int):
    squares, i = [], 1
    while i ** 2 <= n: 
        squares.append(i ** 2)
        i += 1
    lvl = 0
    queue = collections.deque([0])
    visited = []
    while queue:
        lvl += 1
        size = len(queue)
        for i in range(size):
            curr = queue.popleft()
            if curr not in visited:
                # go through neighbors
                for sq in squares:
                    if sq + curr == n: return lvl
                    elif sq + curr > n: break
                    else: queue.append(sq + curr)
    return n

# Time: O(N^2)
# Space: O(N)

def bfsNumSquares2(n: int):
	squares, i = [], 1
	while i ** 2 <= n: 
		squares.append(i ** 2)
		i += 1
	lvl = 0
	queue = collections.deque([n])
	visited = []
	while queue:
		lvl += 1
		size = len(queue)
		for i in range(size):
			curr = queue.popleft()
			if curr in squares: return lvl
			for sq in squares:
				nx = curr - sq
				if nx < 0: break
				if nx not in visited:
					queue.append(nx)
					visited.append(nx)
	return lvl

# Time: O(N^2)
# Space: O(N)