# Write a function:
# that, given a positive integer N, returns the length of its longest binary gap. 
# The function should return 0 if N doesn't contain a binary gap.
# For example, given N = 1041 the function should return 5, 
# because N has binary representation 10000010001
 # so its longest binary gap is of length 5. 
# Given N = 32 the function should return 0, 
# because N has binary representation '100000' and thus no binary gaps.
# N is an integer within the range [1..2,147,483,647].

def solution(N):
   if not 1 <= N <= 2147483647: raise ValueError
   def tobin(N, arr):
       if N > 1:
           tobin(N // 2, arr)
       arr.append(N % 2)
       return arr
   n = tobin(N, [])
   os = [idx for idx, x in enumerate(n) if x == 1]
   n = n[:os[-1] + 1]
   if len(set(n)) == 1: return 0
   res = []
   for i in range(len(os) - 1):
       res.append(os[i + 1] - os[i] - 1)
   localMax = res[0]
   for i in range(1, len(res)):
       if localMax < res[i]:
           localMax = res[i]
   return localMax

print(solution(1041)) # 5
print(solution(32)) # 0

# one liner
def oneLiner(N):
	return len(max(bin(N)[2:].strip('0').strip('1').split('1')))

print(oneLiner(1041)) # 5
print(oneLiner(32)) # 0

