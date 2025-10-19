# https://neetcode.io/problems/anagram-groups?list=neetcode150

from collections import defaultdict

def group_anagrams(strs: list) -> list:
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

testcases = [
    ["act","pots","tops","cat","stop","hat"],   # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    ["x"],                                      # [["x"]]
    [""]                                        # [[""]]
]

print([group_anagrams(x) for x in testcases])


