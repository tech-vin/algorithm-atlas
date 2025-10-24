# https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150

'''
    [2, 4, 6] -> [48]
    [1, 4, 6] -> [48, 24]
    [1, 2, 6] -> [48, 24, 12]
    [1, 2, 4] -> [48, 24, 12, 8]
'''
def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res
    


nums = [1, 2, 4, 6]
print(product_except_self(nums))