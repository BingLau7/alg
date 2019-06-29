import math
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [_i for _i in range(1, n + 1)]
        res = []
        remain_k = k
        for i in range(len(arr)):
            r, remain_k, arr = self.select_num(remain_k, arr)
            res.append(r)
        return ''.join(str(i) for i in res)

    def select_num(self, remain_k: int, arr: List[int]) -> (int, int, List[int]):
        k = math.factorial(len(arr) - 1)
        i = remain_k // k
        remain_res_k = remain_k % k
        if remain_res_k == 0 and i > 0:
            remain_res_k = k
            i -= 1
        res = arr.pop(i)
        return res, remain_res_k, arr


if __name__ == '__main__':
    # n, k = 3, 2
    n, k = 4, 9
    print(Solution().getPermutation(n, k))
