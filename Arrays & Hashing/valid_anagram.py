# https://neetcode.io/problems/is-anagram?list=neetcode150

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s, reverse=True) == sorted(t, reverse=True)

def is_anagram_man(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

testcases = [
    ['racecar', 'carrace'],     # True
    ['jam', 'jar'],             # False
    ['', 'yes'],                # False
    ['', ''],                   # True
    ['yes', '']                 # False
]

print([is_anagram(x[0], x[1]) for x in testcases])
print([is_anagram_man(x[0], x[1]) for x in testcases])