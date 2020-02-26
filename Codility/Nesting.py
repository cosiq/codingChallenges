# A string S consisting of N characters is called properly nested if:
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
# Write a function that, given a string S consisting of N characters, 
# returns 1 if string S is properly nested and 0 otherwise.

def nesting(S):
    paren, stack = {"(": ")"}, []
    for ch in S:
        if ch in paren.keys(): stack.append(paren[ch])
        if ch in paren.values():
            if len(stack) == 0 or ch != stack[-1]: return 0
            elif ch == stack[-1]: stack.pop()
    return int(len(stack) == 0)