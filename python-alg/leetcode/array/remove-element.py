from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for i in nums:
            if i != val:
                result.append(i)
        nums.clear() 
        for i in result:
            nums.append(i)
        return len(result)

if __name__ == '__main__':
    r = [3,2,2,3]
    print(Solution().removeElement(r, 3))
    print(r)