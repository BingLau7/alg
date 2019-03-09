import math

from typing import List

"""
1. 若中间数比最右边小，则右边有序
2. 若中间数比最右边大，则左边有序
3. 根据哪遍有序来判断数在哪个位置
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.search_help(nums, target, 0, len(nums)-1)

    def search_help(self, nums: List[int], target: int, up: int, down: int) -> int:
        if up == down:
            return up if nums[up] == target else -1
        mid = math.floor((down - up) / 2) + up
        if nums[mid] == target:
            return mid

        if nums[mid] > nums[-1] and target > nums[up]: # 左边是有序的且数据可能在左边
            return self.search_2(nums, target, 0, mid)
        elif nums[mid] > nums[-1] and target < nums[up]: # 只能在右边
            return self.search_help(nums, target, mid+1, len(nums)-1)
        elif nums[mid] < nums[-1] and target > nums[mid] : # 右边是有序的且数据可能在右边
            return self.search_2(nums, target, mid+1, len(nums)-1)
        elif nums[mid] < nums[-1] and  target < nums[mid]: # 只能在左边
            return self.search_help(nums, target, up, mid)

    # 二分查找
    def search_2(self, nums: List[int], target: int, up: int, down: int) -> int:
        if up == down:
            return up if nums[up] == target else -1
        t = math.floor((down - up) / 2) + up
        if nums[t] == target:
            return t
        elif target > nums[t]:
            return self.search_2(nums, target, t+1, down)
        else:
            return self.search_2(nums, target, up, t)

if __name__ == '__main__':
    print(Solution().search([5,1,3], 3))
    # print(Solution().search_2([0,1,2,3,4,5,6], 2, 0, 6))