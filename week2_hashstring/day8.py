# Time: O(n)
# Space: O(1)
# DAY 8 — Hashing Deep Dive
# Problem 1: Contains Duplicate

def containsDuplicate(nums):
    seen = set()   #set stores unique values only No duplicates allowed
    for num in nums :
        if num in seen:
            return True
        seen.add(num)
        return False 

nums = [1,2,3,1]
print   (containsDuplicate(nums))

#Problem 2: First Unique Char
def firstUniqChar(chars):
        count = {}

        # Step 1: Count frequency
        for char in chars:
            count[char] = count.get(char, 0) + 1

        # Step 2: Find first unique
        for i in range(len(chars)):
            if count[chars[i]] == 1:
                return i

        return -1

chars = "loveleetcode"
print (firstUniqChar(chars))