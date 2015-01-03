#coding:utf-8

"""
 题目内容：
 给定 n 个数组成的数组，求其逆序对的总数。 逆序对定义为，存在 (i, j) 满足 i < j 且 A[i] > A[j] 的二元组的数目。

 输入格式:
     第一行包含一个整数，表示数组的项数。 接下来的一行，包含 $n$ 个数（$$\leq 100000$$），依次表示 Ai(Ai ≤ 109)。

     输出格式：
     输出一行表示对应的答案。

     输入样例：
     5
     1 3 2 5 4

     输出样例：
     2
"""


class Solution(object):
    """
        "Alg Class"
    """
    pairNum = 0

    def search(self, arr, left, right):
        """
            找逆序对
        """
        if left < right:
            middle = (left+right)/2
            self.search(arr, left, middle)
            self.search(arr, middle+1, right)
            self.merge(left, middle, right, arr)

    def merge(self, left, middle, right, arr):
        """
            合并数组
        """
        left_arr_length = middle-left
        right_arr_length = right-middle
        left_arr = [arr[i] for i in range(left_arr_length+1)]
        right_arr = [arr[middle+i+1] for i in range(right_arr_length)]
        left_arr.append(2000)
        right_arr.append(2000)
        i, j, k = 0, 0, left
        while k < right:
            if left_arr[i] < right_arr[j]:
                i += 1
            else:
                Solution.pairNum += 1
                j += 1
            k += 1

if __name__ == '__main__':
    num = int(raw_input())
    nums = raw_input()
    arr = [int(x) for x in nums.split(' ')]
    i = 0

    test = Solution()
    test.search(arr, 0, num-1)
    print Solution.pairNum
