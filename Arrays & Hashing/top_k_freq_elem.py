from typing import List

def top_k_freq_elements(nums: list, k:int) -> List[int]:
    # base case
    if k == 0:
        return []

    n = len(nums)
    # count the freq
    freq = {}
    for item in nums:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # fill the bucket
    buckets = [[] for _ in range(n + 1)]
    for key, val in freq.items():
        buckets[val].append(key)

    # reverse traverse, return result
    res = []
    for f in range(n, 0, -1):
        if buckets[f]:
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
    return res

testcases = [
    [[1,2,2,2,2,4,4,3,3], 2],
    [[1,2,2,3,3,3], 3],
    [[2,3], 1],
    [[7, 7], 7],
    [[1], 1]
    ,[[1,1,1,1,2,2,3,3,3,4,4,4,4], 3]
]
print([top_k_freq_elements(x, y) for x, y in testcases])