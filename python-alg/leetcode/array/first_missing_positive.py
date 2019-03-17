from typing import List

"""
思路: 
将 index 放在 nums[index] 中，遍历找到 nums[index] != index 的数，index 即是最小，
如果都没有则是 len(nums)
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        nums.insert(0, 0) # 补全 0

        for i in range(1, len(nums)):
            if nums[i] < 0 or nums[i] >= len(nums):
                nums[i] = 0

        for i in range(1, len(nums)):
            if i != nums[i]:
                t = nums[i]
                while nums[t] != t:
                    p = nums[t]
                    nums[t] = t
                    t = p

        for i in range(1, len(nums)):
            if i != nums[i]:
                return i

        return len(nums)

if __name__ == '__main__':
    nums = [3,4,-1,1]
    print(Solution().firstMissingPositive(nums))
    print(nums) 