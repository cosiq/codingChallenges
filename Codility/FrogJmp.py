# A small frog wants to get to the other side of the road. 
# The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
# The small frog always jumps a fixed distance, D.
# Write a function that, given three integers X, Y and D, 
# returns the minimal number of jumps from position X to a position 
# equal to or greater than Y.
# For example, given: X = 10   Y = 85   D = 30, the function should return 3

def frogJmp(X, Y, D):
	if X == Y: return 0
	q, r = divmod(Y - X, D)
	return q + 1 if r != 0 else q


frogJmp(10, 85, 30) # 3

# Time: O(1)
# Space: O(1)