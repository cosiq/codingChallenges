# Given a non-empty array of non-negative integers nums, the degree of this array is defined 
# as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
# that has the same degree as nums.
# Example 1:
#	 Input: [1, 2, 2, 3, 1]
#	 Output: 2
# Explanation: The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
#	 Input: [1,2,2,3,1,4,2]
#	 Output: 6

def shortestSubArray(nums):
	cmp = {}
    for idx, x in enumerate(nums):
        if x in cmp: cmp[x].append(idx)
        else: cmp[x] = [idx]
    res = max([len(item) for item in cmp.values()])
    return min([item[-1] - item[0] for item in cmp.values() if len(item) == res]) + 1

# Time: O(N)
# Space: O(N)


def findShortestSubArray(nums):
    if nums == []: return 0
    cmp = {}
    for n in nums:
        if n not in cmp: cmp[n] = 1
        else: cmp[n] += 1
    degree = max(cmp.values())
    if degree == 1: return 1
    else:
        minLength = len(nums)
        for keys in cmp:
            if cmp[keys] == degree:
                pos1 = nums.index(keys)
                pos2 = len(nums) - nums[::-1].index(keys) - 1
                if pos2 - pos1 + 1 < minLength:
                    min_length = pos2 - pos1 + 1
    return minLength
    
# Time: O(N)
# Space: O(N)
