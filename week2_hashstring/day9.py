# Time: O(n)
# Space: O(1)
# DAY 8 — Hashing Deep Dive
# Problem 1: Valid Anagram
def isAnagram(char1, char2):
        if len(char1) != len(char2) :
                return False
        count = {}
        for char in char1:
            count[char] = count.get(char, 0) + 1
            
        for char in char2:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True

char1 = "anagram" 
char2 = "nagaram"
print(isAnagram(char1, char2))

#Problem 2: Find All Anagrams in a String
from collections import Counter

def findAnagrams(s, p):
    s_len, p_len = len(s), len(p)
    if s_len < p_len:
        return []

    p_count = Counter(p)
    s_count = Counter()
    result = []

    for i in range(s_len):
        # Add a character from the right
        s_count[s[i]] += 1
        
        # Remove a character from the left if window exceeds size p_len
        if i >= p_len:
            if s_count[s[i - p_len]] == 1:
                del s_count[s[i - p_len]]
            else:
                s_count[s[i - p_len]] -= 1
        
        # Compare window with p_count
        if p_count == s_count:
            result.append(i - p_len + 1)
            
    return result

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))