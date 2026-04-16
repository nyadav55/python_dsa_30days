# Time: O(n)
# Space: O(1)
# Problem 1: Missing Number
#🧠 Given array with numbers from 0 → n
#👉 One number is missing → find it
"""
nums = [3,0,1]
o/p = 2
"""
def missingNumber(nums):
    nj = len(nums)
    for i in range(len(nums)):
        nj ^= i ^ nums[i]

    return nj    

nums = [3,0,1]
print(missingNumber(nums))

# Problem 2: Find the Duplicate Number
# One number repeats → find it
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # find entry
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1,3,4,2,2, 1]
print(findDuplicate(nums))