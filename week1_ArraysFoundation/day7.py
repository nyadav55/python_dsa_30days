# Time: O(n)
# Space: O(1)
# DAY 7 — Revision last 6 days + Real Interview Patterns
# Problem 1: Best Time to Buy & Sell Stock
#👉 Buy at lowest price 👉 Sell at highest profit later
# [7,1,5,3,6,4] → Output: 5

def maxProfit(prices):
    minprice = float('inf') # 7 start with very large value
    profit = 0

    for price in prices:
        minprice = min(minprice, price) #1  
        profit = max(profit, price - minprice)
    return profit

prices = [7,1,5,3,6,4]
print (maxProfit(prices))

# Problem 2: Contains Duplicate
#👉 array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    seen = set()   #set stores unique values only No duplicates allowed
    for num in nums :
        if num in seen:
            return True
        seen.add(num)
    return False    

nums = [1,2,3,1]
print (containsDuplicate(nums))

"""
🎯 DAY 7 SUMMARY
✅ HashMap
✅ Two Pointer
✅ Binary Search
✅ Math + XOR
✅ Cycle Detection
✅ Greedy
"""