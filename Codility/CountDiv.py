# Write a function that, given three integers A, B and K, 
# returns the number of integers within the range [A..B] that are divisible by K, 
# i.e.: { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, 
# because there are three numbers divisible by 2 within the range [6..11], 
# namely 6, 8 and 10.

def countDiv(A, B, K):
	if A % K == 0: return (B - A) // K + 1
	else: return (B - (A - A % K)) // K

# Time: O(1)
# Space: O(1)