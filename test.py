# encoding:utf-8
"""
    测试
"""
import time

def main(data):
    """
        执行函数
    """
    print 321 in data

if __name__ == '__main__':
    data = list()
    for i in range(10000000):
        data.append(i)
    start = time.clock()
    main(data)
    end = time.clock()
    print end - start
