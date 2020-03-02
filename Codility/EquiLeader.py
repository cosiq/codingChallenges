# A non-empty array A consisting of N integers is given.
# The leader of this array is the value that occurs in more than half of the elements of A.
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] 
# and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

# For example, given array A such that:
# 	A[0] = 4	A[1] = 3	A[2] = 4	A[3] = 4	A[4] = 4	A[5] = 2

# we can find two equi leaders:
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.

# Write a function that, given a non-empty array A consisting of N integers, 
# returns the number of equi leaders.


def equiLeader(A):
    n, cmp = len(A), sorted(A)
    median = cmp[len(cmp)//2]
    cnt, lst = 0, []
    
    for a in A:
        if a == median: cnt += 1
        lst.append(cnt)

    res = 0
    for i in range(n):
        if ((i + 1) / 2 < lst[i] and 
        (n - i - 1) / 2 < cnt - lst[i]):
            res += 1

    return res


# Time: O(N)
# Space: O(N)