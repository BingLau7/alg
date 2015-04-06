#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if target <= A[i]:
                return i
        return len(A)

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 0)

