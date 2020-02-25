# Write a function that, given a non-empty array A, 
# returns the value of the maximal product of any triplet.
# For example, given array A such that:
# 	A[0] = -3	A[1] = 1	A[2] = 2	A[3] = -2	A[4] = 5	A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.
def maxProductTriplet(A):
    A = sorted(A)
    # if mixed
    if max(A) > 0 and min(A) < 0: return max(A[0] * A[1], A[-2] * A[-3]) * A[-1]
    return A[-1] * A[-2] * A[-3]