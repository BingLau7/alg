#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = list(bin(n)[2:])
        return len([i for i in num if i != '0'])

if __name__ == '__main__':
    print(Solution().hammingWeight(11))
