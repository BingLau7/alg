from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self._combine(res, 1, n, k, [])
        return res

    def _combine(self, res, i: int, n: int, k: int, temp):
        if k == 0:
            res.append(temp)
            return
        for j in range(i, n + 1):
            temp_2 = temp.copy()
            temp_2.append(j)
            self._combine(res, j+1, n, k - 1, temp_2)


if __name__ == '__main__':
    n, k = 4, 3
    print(Solution().combine(n, k))
