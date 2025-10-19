# https://neetcode.io/problems/two-integer-sum?list=neetcode150

def two_sum(nums: list, t: int) -> list[int, int]:
    seen = {}
    for indx, val in enumerate(nums):
        compliment = t - val
        if compliment in seen:
            return [indx, seen[compliment]]
        seen[val] = indx
    return []


testcases = [
    [[3, 4, 5, 6], 7],     # [0, 1]
    [[4, 5, 6], 10],    # [0, 2]
    [[5, 5], 10],       # [0, 1]
]
print([two_sum(x[0], x[1]) for x in testcases])