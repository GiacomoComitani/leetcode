from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res * (1 << (len(nums) - 1))

nums = [5, 1, 6]
sol = Solution()
print(sol.subsetXORSum(nums))  
