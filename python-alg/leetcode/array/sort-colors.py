from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


if __name__ == '__main__':
    # nums = [0, 1, 0]
    # nums = [0]
    nums = [2, 0, 2, 1, 1, 0]
    # nums = [2, 0]
    # nums = [2, 0, 1]
    # nums = [0, 0, 1, 0, 1, 1]
    print(Solution().sortColors(nums))
    print(nums)
