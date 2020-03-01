# Write a function that, given an array A describing N discs as explained above, 
# returns the number of (unordered) pairs of intersecting discs. 
# The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
# Given array A shown above, the function should return 11, as explained above.

def numbersDisc(A):
    cnt = 0
    for i in range(len(A) - 1):
        lw, up = i - A[i], i + A[i]
        for j in range(i + 1, len(A)):
            if (lw >= j - A[j] and up <= j + A[j]) or (lw <= j + A[j] and up >= j - A[j]):
                cnt += 1
    if cnt > 10E6: return -1
    return cnt


# Time: O(N^2)
# Space: O(1)

    










