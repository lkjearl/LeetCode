class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sortedArray = []
        for i in nums:
            if i % 2 == 0:
                sortedArray.append(i)
        for i in nums:
            if i % 2 != 0:
                sortedArray.append(i)
        return sortedArray