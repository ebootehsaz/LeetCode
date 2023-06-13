def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []

    for i in s:
        if i == '}':
            if len(stack) == 0: return False
            left = stack.pop()
            if left != '{': return False 
        elif i == ']':
            if len(stack) == 0: return False
            left = stack.pop()
            if left != '[': return False 
        elif i == ')':
            if len(stack) == 0: return False
            left = stack.pop()
            if left != '(': return False 
        else:
            stack.append(i)

    return len(stack) == 0


print(isValid("()[]([)]")) # false
print(isValid("()[]{}"))   # true
print(isValid("(]"))       # false
print(isValid("()[]([)]")) # false
print(isValid("]"))       # false