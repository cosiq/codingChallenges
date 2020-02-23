# A left rotation operation on an array of size n 
# shifts each of the array's elements 1 unit to the left.
# For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5]
# then the array would become [3, 4, 5, 1, 2]
# Given an array of n integers and a number d, perform d left roattions on the array.
# Then print the updated array as a single line of space-separated integers
# Input Format:
# d: the number of left rotations you must perform
# array: n space-separated integers describing 
# the respective elements of the array's initial state.
# Constraints:
# 1 <= n <= 10^5
# 1 <= d <= n
# 1 <= a_i <= 10^6
# Output Format:
# Print a single line of n space-separated integers denoting the final state of the array
# after performing d left rotations

def leftRotation(d, arr):
	d %= len(arr)
	a[:] = a[d:] + a[:d]
	print(*a, sep=" ")

leftRotation(4, [1, 2, 3, 4, 5]) # 5 1 2 3 4