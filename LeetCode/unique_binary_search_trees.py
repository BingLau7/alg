#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return an integer
    def numTrees(self, n):
        """
            选出其中第k个结点，比k小的在左边，比k大的在右边，有n种选择
            这么想：当其中有一个结点确定的时候，左边就是numTrees(k-1),
            右边相当于numTrees(n-k),这时候所产生的组合数就为numTrees(k-1)*numTrees(n-k),
            可以使用动态规划解决
        """
        num = [None] * (n + 1)
        num[0] = 1
        i = 0
        while i <= n:
            k = 1
            if num[i] == None:
                num[i] = 0
                while k <= i:
                    num[i] += num[k-1] * num[i-k]
                    k += 1
            i += 1
        return num[n]

if __name__ == '__main__':
    print Solution().numTrees(4)
