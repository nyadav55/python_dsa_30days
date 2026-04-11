# Time: O(n)
# Space: O(1)
# Problem 1: Reverse String
#🧠 Problem Statement (Simple)
# Reverse a list of characters in-place
# Example - Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse_String(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

s = ["h","e","l","l","o"]
print (reverse_String(s))

# Problem 2: Monotonic Array

# Check if array is: Increasing OR Decreasing
#📌 Example [1,2,3,4] → True  [4,3,2,1] → True  [1,3,2] → False 

def isMonotonic(nums):
    incrs = True
    decrs = True
    for i in range(len(nums)-1):
        if(nums[i] > nums[i+1]):
            incrs = False
        if nums[i] > nums[i+1]:
            decrs = False
    return    incrs  or  decrs       

nums = [1,2,6,4,5]
print (isMonotonic(nums))