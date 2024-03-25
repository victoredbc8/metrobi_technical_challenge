def are_brackets_balanced(s):
    stack = []
    brackets_map = {
        ')': '(', 
        ']': '[', 
        '}': '{',
    }

    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or brackets_map[char] != stack[-1]:
                return False
            stack.pop()
        else:
            return False
    
    return not stack

# Exemples provided
print(are_brackets_balanced("{[]}"))
print(are_brackets_balanced("{(])}"))
print(are_brackets_balanced("{([)]}"))
