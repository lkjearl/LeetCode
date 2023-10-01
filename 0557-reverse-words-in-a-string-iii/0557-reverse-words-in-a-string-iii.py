class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reverseWords = []

        for word in words:
            reverseWords.append("".join(word[::-1]))
        return " ".join(reverseWords)