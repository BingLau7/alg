#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a string
    def convertToTitle(self, num):
        """
            10进制转换为26进制
        """
        result = ''
        while num:
            tmp = num % 26
            if not tmp:
                result += 'Z'
                num = num / 26 -1
            else:
                result += chr(64 + tmp)
                num /= 26
        return result[::-1]

if __name__ == '__main__':
    print Solution().convertToTitle(52)
