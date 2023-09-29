class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        startIndex = 0
        buffer = []

        i = 0
        while i < len(s):
            if s[i] in buffer:
                if maxLength < len(buffer):
                    maxLength = len(buffer)
                    buffer.clear()
                else:
                    buffer.clear()
                startIndex += 1
                i = startIndex
            else:
                buffer.append(s[i])
                i += 1
        if maxLength < len(buffer):
            maxLength = len(buffer)
        return maxLength