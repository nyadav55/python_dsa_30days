# Time: O(n)
# Space: O(1)
# Problem 1: Search Insert Position
#🧠 Problem Statement (Simple)
"""
Given a sorted array, find:
If target exists → return index
If not → return position where it should be inserted
"""
def sip(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

nums = [1,3,5,6,7,2,6]
target = 6

print(sip(nums, target))

# Problem 2: First Unique Character
# Find first character that appears only once

def firstUniqChar(s):    
    count = {}

    # Step 1: Count frequency
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Step 2: Find first unique
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1

s = "lettcode"
print(firstUniqChar(s))

