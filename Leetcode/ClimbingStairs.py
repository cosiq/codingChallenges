# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# Example 1:
#	 Input: 2
#	 Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
#	 Input: 3
#	 Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n: int):
	lst, idx = [1, 1], 2
	while idx <= n:
		lst.append(lst[idx  - 1] + lst[idx - 2])
		idx += 1
	return lst[n]

# Time: O(N)
# Space: O(N)

def idxClimbStairs(n: int):
    prev, curr = 1, 1
    while n >= 1 :
        prev, curr = curr, curr + prev
        n -= 1
    return prev   

# Time: O(N)
# Space: O(1)