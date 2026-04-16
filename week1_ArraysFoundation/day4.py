# Time: O(n)
# Space: O(1)
# Problem 1: Move Zeroes
#🧠 Move all 0s to the end
"""
nums = [0,1,0,3,12]
o/p = [1,3,12,0,0]
"""
def moveZeroes(nums):
        x = 0
        for i in nums:
            if i != 0:
                nums[x] = i
                x += 1
        for a in range(x, len(nums)):
            nums[a] = 0

nums = [0,1,0,3,12]
print(moveZeroes(nums))

# Problem 2: Remove Duplicates (Sorted Array)
# Remove duplicates in-place
def removeDuplicates(nums):
     i = 0
     for j in range(1, len(nums)):
          if nums[j] != nums[i]:
               i += 1
               nums[i] = nums[j]
     return i + 1          

nums = [1,1,2,2,3, 3, 3, 4]
print(removeDuplicates(nums))