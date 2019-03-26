from typing import List

class Solution:

    # f(m, n) = f(m-1, n) + f(m, n-1)
    # f(1, 1) = 1, f(1, 2) = 1, f(2, 1) = 1
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0 for i in range(n + 1)] for i in range(m + 1)]
        mem[1][1] = 1 
        if n > 3:
            mem[1][2] = 1
        if m > 3:
            mem[2][1] = 1
        return self.helper(m, n, mem)

    def helper(self, m: int, n: int, mem: List[List[int]]) -> int:
        if mem[m][n] == 0 and m != 0 and n != 0:
            result = self.helper(m-1, n, mem) + self.helper(m, n-1, mem)
            mem[m][n] = result
            return result
        return mem[m][n]

if __name__ == '__main__':
    print(Solution().uniquePaths(m=23, n=12))