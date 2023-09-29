class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        index = {}
        
        for i, char in enumerate(s):
            if char in index and index[char] >= start:
                start = index[char] + 1
            
            index[char] = i
            currentLength = i - start + 1
            maxLength = max(maxLength, currentLength)
        
        return maxLength