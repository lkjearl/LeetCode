class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0
        
        # Calculate the length of the decoded string
        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1
        
        # Work backward to find the k-th character
        for char in reversed(s):
            k %= decoded_length
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                decoded_length //= int(char)
            else:
                decoded_length -= 1