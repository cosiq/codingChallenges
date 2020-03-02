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


# def numbersDisc(A):
#     events = []
#     for i, a in enumerate(A):
#         events += [(i-a, +1), (i+a, -1s#     events.sort(key=lambda x: (x[0], -x[1]))
#     intersections, active_circles = 0, 0
#     for _, circle_count_delta in events:
#         intersections += active_circles * (circle_count_delta > 0)
#         active_circles += circle_count_delta
#         if intersections > 10E6: return -1
#     return intersections

# Time: O(N)
# Space: O(N)
