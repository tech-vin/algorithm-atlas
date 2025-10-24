# https://neetcode.io/problems/is-palindrome?list=neetcode150

def is_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    result = ''
    for ch in string.lower():
        if ch.isalnum():
            result = ch + result
    return result == string

testcases = ['listen', 'mom', 'wow']
print([is_palindrome(x) for x in testcases])