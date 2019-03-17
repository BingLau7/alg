from typing import List

"""
1. 若中间数比最左边大，则左边有序，否则右边有序
2. 判断哪边有序之后，判断目标数在哪边位置，递归查找
3. 根据哪遍有序来判断数在哪个位置
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            
            if nums[mid] >= nums[low]: # 左边升序
                if target >= nums[low] and target < nums[mid]: # target 在左边范围，收缩范围二分查找
                    high = mid - 1
                else: # target 在右边范围，收缩范围二分查找
                    low = mid + 1
            else: # 右边升序
                if target > nums[mid] and target <= nums[high]: # target 在右边范围，收缩范围二分查找
                    low = mid + 1
                else: # target 在左边范围，收缩范围二分查找
                    high = mid - 1
        return -1

if __name__ == '__main__':
    print(Solution().search([5,1,3], 5))
    # print(Solution().search_2([0,1,2,3,4,5,6], 2, 0, 6))