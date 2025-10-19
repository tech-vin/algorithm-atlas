# https://neetcode.io/problems/duplicate-integer?list=neetcode150

def contains_duplicate(arr):
    if len(arr) <= 1:
        return True
    
    seen = {}

    for item in arr:
        if item in seen:
            return True
        seen[item] = 1

    return False


testcases = [
    [1, 2, 3, 3],   # True
    [],             # True
    [1],            # True
    [1, 2, 3, 4]    # False
]

print([contains_duplicate(x) for x in testcases])