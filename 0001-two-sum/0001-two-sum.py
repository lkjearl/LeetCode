class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i, num in enumerate(nums):
            if remainder and (target - num) in remainder:
                return [remainder[(target - num)], i]
            
            remainder[num] = i