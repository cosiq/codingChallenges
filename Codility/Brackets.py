# Write a function that, given a string S consisting of N characters, 
# returns 1 if S is properly nested and 0 otherwise.
# For example, given S = "{[()()]}", the function 
# should return 1 and given S = "([)()]", the function should return 0, as explained above.

def brackets(S):
	paren = {"{":"}", "[":"]", "(": ")"}
    queue = []
    for ch in S:
        if ch in paren.keys(): queue.append(paren[ch])
        if ch in paren.values():
            if len(queue) == 0 or ch != queue[-1]: return 0
            elif ch == queue[-1]: queue.pop()
    return len(queue) == 0