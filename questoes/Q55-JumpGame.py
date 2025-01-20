class Solution:
    def canJump(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            # Se já alcançamos o último índice, podemos parar.
            if max_reach >= len(nums) - 1:
                return True
        return False
