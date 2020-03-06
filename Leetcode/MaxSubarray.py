# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Example:
#	 Input: [-2,1,-3,4,-1,2,1,-5,4],
#	 Output: 6
#	 Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums: List[int]):
	
	localMax, globalMax = nums[0], nums[0]
    for i in range(1, len(nums)):
        localMax = max(nums[i], localMax + nums[i])
        if localMax > globalMax: globalMax = localMax
    return globalMax
    
# Time: O(N)
# Space: O(1)

        