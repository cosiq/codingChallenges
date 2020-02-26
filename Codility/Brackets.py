# Write a function that, given a string S consisting of N characters, 
# returns 1 if S is properly nested and 0 otherwise.
# For example, given S = "{[()()]}", the function 
# should return 1 and given S = "([)()]", the function should return 0, as explained above.


def brackets(S):

	paren, stack = {"{":"}", "[":"]", "(": ")"}, []
    for ch in S:
        if ch in paren.keys(): stack.append(paren[ch])
        if ch in paren.values():
            if len(stack) == 0 or ch != stack[-1]: return 0
            elif ch == stack[-1]: stack.pop()
    return len(stack) == 0

