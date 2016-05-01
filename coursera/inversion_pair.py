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
import sys

INF = float('inf')
pair_num = 0    #逆序对数


def mergesort(arr):
    """
        归并排序
    """
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)/2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        result = merge(left, right)
        return result

def merge(left, right):
    """
        归并数组
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            global pair_num
            #排序之后left后面肯定比前面大，计数的时候需要把后面的数也算上去
            #比如135246中,(3,2)逆序则(5,2)也逆序
            pair_num += len(left) - i
            result.append(right[j])
            j += 1


    #i, j是在外部定义的，也就是说i，j位置之后的数值是正确顺序排列的
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    #其结果作为局部返回
    return result

if __name__ == '__main__':
    arr = list()

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        arr.append(int(line))

    print mergesort(arr)
    print pair_num
