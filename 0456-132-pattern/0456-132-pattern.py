class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []
        # '2' in 132
        secondNum = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < secondNum:
                return True

            while stack and nums[i] > stack[-1]:
                secondNum = stack.pop()

            stack.append(nums[i])

        return False