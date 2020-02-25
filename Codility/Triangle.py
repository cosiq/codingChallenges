# Write a function that, given an array A consisting of N integers, 
# returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
# For example, given array A such that:
# 	A[0] = 10	A[1] = 2	A[2] = 5	A[3] = 1	A[4] = 8	A[5] = 20
# the function should return 1, as explained above. 
# Given array A such that:
#   A[0] = 10	A[1] = 50	A[2] = 5	A[3] = 1
# the function should return 0.

def triangle(A):
    length = len(A)
    if length < 3: return 0
    A = sorted(A)
    for i in range(length - 2):
        if A[i] + A[i+1] > A[i + 2]: return 1
    return 0