# Time Complexity - O(n) → FAST - $We visit each of the $n$ elements exactly once.
# Space Complexity - O(n) → FAST - $We only use a fixed amount of extra space (two variables), regardless of array size.

# Problem 1: Two Sum Find Max / Min in Array
#🧠 Problem Statement (Simple)
#You are given:
#List of numbers, A target number
#👉 Find 2 numbers that add up to target, 👉 Return their indexes 

def twoSum(number, target):
    store = {}
    for i in range(len(number)):
        num = number[i]
        result = target - num
        if result in store:
            return [store[result], i]

        store[num] = i

number = [3,2,4]
target = 5  
print(twoSum(number, target))    

# Problem 2: Maximum Subarray
#🧠 Problem Statement (Simple)
#Find maximum sum of contiguous subarray

def maxSubArray(number):
    current_sum = number[0]
    max_sum = number[0]

    for num in number[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum    

number = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(number)) 

"""
🎯 DAY 1 SUMMARY - learned:
✅ Brute force vs optimized
✅ HashMap pattern
✅ Kadane’s algorithm
✅ Time complexity thinking
"""