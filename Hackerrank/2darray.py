# Given a 6 * 6 2D array, arr.
# We define an hourglass in A to be a subset of values with indices 
# falling in this pattern n array's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in arr, then print the maximum.
# Input Format: 
# Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j]
# Constraints:
# -9 <= arr[i][j] <= 9
# 0 <= i,j <= 5
# Output Format:
# Print the largest (maximum) hourglass sum found in arr.

def hourglassSum(arr):
    # 1. set a frame 3*3 for each flop
    # 2. calculate hourglass values and store them

    def helper(matrix):
        s = 0
        num = len(matrix)
        for i in range(num):
            for j in range(num):
                s += matrix[i][j]
        s -= matrix[num // 2][0] + matrix[num // 2][-1]
        return s

    n, res = len(arr), []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            matrix = []
            matrix.append(arr[i - 1][j - 1:j + 2])
            matrix.append(arr[i][j - 1:j + 2])
            matrix.append(arr[i + 1][j - 1:j + 2])
            res.append(helper(matrix))
    return max(res)

ex = [[1,1,1,0,0,0],
      [0,1,0,0,0,0],
      [1,1,1,0,0,0],
      [0,0,2,4,4,0],
      [0,0,0,2,0,0],
      [0,0,1,2,4,0]]

 print(hourglassSum(ex)) # 19