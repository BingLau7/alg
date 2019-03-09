from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        down_index = 0
        # 倒序找下降点
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                down_index = i - 1 
                break

        # 特殊情况，全降序，最大值
        if down_index == 0 and nums[0] > nums[1]:
            nums.reverse()
            return

        change_index = down_index + 1
        min_n = float('inf')
        # 找上升点之前尽可能大的点
        for i in range(len(nums)-1, down_index+1, -1):
            if nums[i] < min_n and nums[i] > nums[down_index]:
                min_n = nums[i]
                change_index = i
        print(down_index, change_index)
        # 交换最大点
        nums[change_index], nums[down_index] = nums[down_index], nums[change_index]
        # 最后集体反转形成一个有了较高位的最小数
        nums[down_index+1:len(nums)] = nums[down_index+1:len(nums)][::-1]


if __name__ == '__main__':
    nums = [2,2,7,5,4,3,2,2,1]
    Solution().nextPermutation(nums)
    print(nums)
        