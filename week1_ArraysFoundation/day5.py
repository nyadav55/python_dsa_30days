# Time: O(n)
# Space: O(1)
# Problem 1: Rotate Array
#🧠 Rotate array to the right by k steps
"""
nums = [1,2,3,4,5,6,7]
k = 3
o/p = [5,6,7,1,2,3,4]
"""
def rotate(nums,k):
    n = len(nums)
    k = k % n   # important

    # helper function
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))

# Problem 2: Third Maximum Numbery
#🧠 Rotate array to the right by k steps
"""
Find 3rd distinct maximum number
👉 If not exist → return max
"""
def third_max(nums):
    first = second = third = None
    for num in nums:
        if num in (first, second, third):
            continue

        if first is None or num > first:
            third = second
            second = first
            first = num

        elif second is None or num > second:
            third = second
            second = num

        elif third is None or num > third:
            third = num

    return third if third is not None else first

nums = [2,2,3,1]
print(third_max(nums))