#!/usr/bin/env python
# encoding: utf-8

"""
The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative (there might
be some repetitions!).This is your array of integers, with the ith row of the
file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x,y in the
input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a
one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space
provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing
your own hash table for it. For example, you could compare performance under
the chaining and open addressing approaches to resolving collisions.

中文描述：设T是一组数，答案求出该数组中两两相加结果不同且结果属于[-10000,10000]
的数量
"""
import sys

def get_sum_result_numeric(data, data_rep):
    """
        实现算法
    """
    result = 0
    tmp_result = set()
    for i in data_rep:
        tmp = i + i
        print 'test---', tmp
        if -10000 <= tmp <= 10000 and tmp not in tmp_result:
            print tmp, '=', i, '+', i
            tmp_result.add(tmp)
            result += 1

    for i in range(-10000, 10001):
        if i in tmp_result:
            continue
        for j in data:
            k = i - j
            if k in data and k != j:
                print i, '=', k, '+', j
                result += 1
                break

    print result


def main():
    """
        执行函数
    """
    data = set()
    data_rep = set()
    i = 0
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = int(line)
        if line in data:
            data_rep.add(line)
        else:
            data.add(line)

    get_sum_result_numeric(data, data_rep)

if __name__ == '__main__':
    main()
