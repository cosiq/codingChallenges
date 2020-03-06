# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.

# Example:
# 	Input: [4,3,2,7,8,2,3,1]
# 	Output: [5,6]

def findDisappearedNumbers(nums: List[int]):
	for n in nums:
        index= abs(n) - 1
        nums[index] = -abs(nums[index])
    return [i+1 for i in range(len(nums)) if nums[i] > 0]


# Time: O(N)
# Space: O(N)

def oneLiner(nums): return set(range(1,len(nums) + 1)).difference(set(nums))

# Time: O(N)
# Space: O(N)
