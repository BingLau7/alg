#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a string
    def convertToTitle(self, num):
        """
             Memory Limit Exceeded
        """
        if num == 0:
            return ''
        if (num % 26) == 0:
            result = 'A' * (num / 26 - 1)
            result += chr(64 + 26)
        else:
            result = 'A' * (num / 26)
            result += chr(64 + num%26)
        return result

    def convertToTitle2(self, num):
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
    print Solution().convertToTitle2(52)
