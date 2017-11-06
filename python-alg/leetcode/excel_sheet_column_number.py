#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        """
            26进制与10进制的转换
        """
        num = 0
        i = 0
        s = s[::-1]
        while i < len(s):
            num += (ord(s[i]) - ord('A') + 1) * pow(26, i)
            i += 1
        return num

if __name__ == '__main__':
    print(Solution().titleToNumber('AB'))

