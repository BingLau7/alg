from typing import List


class Solution:
    # m[i, j] = min(m[i-1, j], m[i, j-1]) + v[i, j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        if n == 1:
            return sum(grid[0])
        if m == 1:
            return sum([a[0] for a in grid])

        mem = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                up = 0
                left = 0
                if i > 0:
                    up = mem[i-1][j]
                if j > 0:
                    left = mem[i][j-1]

                if i == 0:
                    mem[i][j] = left + grid[i][j]
                elif j == 0:
                    mem[i][j] = up + grid[i][j]
                else:
                    mem[i][j] = min(left, up) + grid[i][j]

        return mem[n-1][m-1]


if __name__ == '__main__':
    _input = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(_input))
