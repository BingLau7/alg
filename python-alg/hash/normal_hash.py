# coding=utf-8

"""文件描述
"""
from hashlib import md5
from struct import unpack_from

ITEMS = 10000000
NODES = 100
NEW_NODES = 101

node_stat = [0 for i in range(NODES)]

# 桶大小改变之后映射的改变值
change = 0

for item in range(ITEMS):
    k = md5(str(item)).digest()
    # Unpack from buffer starting at position offset, according to the
    # format string fmt. The result is a tuple even if it contains exactly one item.
    # >: big-endian
    # I: unsigned int
    h = unpack_from(">I", k)[0]
    n = h % NODES
    # 现映射结果
    n_new = h % NEW_NODES
    if n_new != n:
        change += 1
    node_stat[n] += 1

_ave = ITEMS / NODES
_max = max(node_stat)
_min = min(node_stat)

if __name__ == '__main__':
    print("Ave: %d" % _ave)
    print("节点最多的桶:%d 节点数:%d 占比(%0.2f%%)" % (node_stat.index(_max), _max, (_max - _ave) * 100.0 / _ave))
    print("节点最少的桶:%d 节点数:%d 占比:(%0.2f%%)" % (node_stat.index(_min), _min, (_ave - _min) * 100.0 / _ave))
    print("Change: %d\t(%0.2f%%)" % (change, change * 100.0 / ITEMS))
