"""
Problem 10: Write a function unique to find all the unique elements of a list.
"""

def unique(nums):
    r_nums = []
    for x in nums:
        if x in r_nums:
            continue
        r_nums.append(x)
    return r_nums

print unique([1, 2, 1, 3, 2, 5])

"""
Output:
[1, 2, 3, 5]
"""


