from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return [self.findFirst(nums, target, mid), self.findLast(nums, target, mid)]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]


    def findFirst(self, nums: List[int], target: int, equalPos: int) -> int:
        firstIndex = equalPos
        while firstIndex > 0:
            if nums[firstIndex] == target:
                firstIndex -= 1
            else:
                break
        return firstIndex + 1 if (firstIndex != 0 or nums[0] != target) else 0

    def findLast(self, nums: List[int], target: int, equalPos: int) -> int:
        n = len(nums)
        lastIndex = equalPos
        while lastIndex < n:
            if nums[lastIndex] == target:
                lastIndex += 1
            else:
                break
        return lastIndex - 1

if __name__ == '__main__':
    nums = [1, 4]
    solution = Solution()
    # print('first:', solution.findFirst(nums, 4, 1))
    # print('last:', solution.findLast(nums, 1, 0))
    print(solution.searchRange(nums, 4))