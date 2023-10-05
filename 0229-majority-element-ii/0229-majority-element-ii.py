class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        returned = []
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

            if num not in returned and seen[num] > len(nums)/3:
                returned.append(num)
        return returned