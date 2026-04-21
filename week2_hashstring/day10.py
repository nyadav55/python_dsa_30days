# Time: O(n)
# Space: O(1)
# DAY 10 — Hashing Deep Dive
# Problem 1: Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Agar character pehle mil chuka hai aur window ke andar hai
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

# Problem 2: Reverse Words in a String

def reverseWords(s):
    # split() automatically saare extra spaces handle kar leta hai
    words = s.split()
    # Words ko reverse karo aur single space se join kar do
    return " ".join(words[::-1])
s = "the sky is blue"
print (reverseWords(s))