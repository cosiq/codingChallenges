# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Example:
#	 Input: [0,1,0,3,12]
#	 Output: [1,3,12,0,0]

def moveZeros(nums: List[int]):
	idx = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[idx], nums[i] = nums[i], nums[idx]
			idx += 1

# Time: O(N)
# Space: O(1)