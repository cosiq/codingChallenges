# An array A consisting of N integers is given. 
# The dominator of array A is the value that occurs in more than half of the elements of A.

# For example, consider array A such that
#   A[0] = 3    A[1] = 4    A[2] =  3   A[3] = 2    A[4] = 3    A[5] = -1   A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A 
# (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

# Write a function that, given an array A consisting of N integers, 
# returns index of any element of array A in which the dominator of A occurs. 
# The function should return −1 if array A does not have a dominator.


def solution(A):
    if len(A) == 0: return -1
    book = {item:0 for item in set(A)}
    for item in A:
        if item in book: book[item] += 1
    new = sorted(book.items(), key=lambda x: x[1], reverse=True)
    if new[0][1] > len(A) / 2: 
        val = new[0][0]
        return [idx for idx, x in enumerate(A) if x == val][0]
    return -1

# Time: O(N)
# Space: O(N)

def usingStacks(A):
    stack = []
    for item in A:
        stack.append(item)
        while len(stack) > 1 and stack[-1] != stack[-2]:
            stack.pop(), stack.pop()
    if stack:
        head, cnt = stack[0], 0
        for idx, x in enumerate(A):
            if x == head: cnt += 1
            if cnt > len(A) / 2: return idx
    return -1

# Time: O(N)
# Space: O(N)