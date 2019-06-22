from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 采用铺路的思路进行解决
        if len(nums) <= 1:
            return True
        i = 1
        # 剩余步数
        remain = nums[0]
        if remain == 0:
            return False
        while i < len(nums) and remain < len(nums):
            remain = max(remain, nums[i] + 1) - 1
            if remain == 0 and i != len(nums) - 1:
                return False
            elif i == len(nums) - 1:
                return True
            i += 1

        return True


if __name__ == '__main__':
    _input = [3,2,1,0,4]
    print(Solution().canJump(_input))
