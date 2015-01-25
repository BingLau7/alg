#!/usr/bin/env python
# encoding: utf-8

"""
    图算法
"""
class Graph(object):
    """
        无权无向图
    """
    def __init__(self, v_num):
        self.index = 0      #迭代器
        self.edge_num = 0   #边数
        self.v_set = list([None]*v_num)     #结点集合
        for i in range(v_num):
            self.v_set[i] = set()

    def add_edge(self, v_node, w_node):
        """
            连接v,w的边
        """
        self.v_set[v_node].add(w_node)
        self.v_set[w_node].add(v_node)
        self.edge_num += 1

    def get_degree(self, v_node):
        """
            得到v结点的度数
        """
        degree = len(self.v_set[v_node])
        return degree

    def __iter__(self):
        return iter(self.v_set)

def main():
    """
        测试函数
    """
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    for index, i in enumerate(graph):
        print index,
        for j in i:
            print j,
        print

if __name__ == '__main__':
    main()
