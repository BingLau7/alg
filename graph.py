#!/usr/bin/env python # encoding: utf-8

"""
求最小分割
"""

import sys
import random

class Adj(object):
    """
        一个（或多个顶点合一）邻接边
    """
    def __init__(self, vertices, edge):
        self.vertices = vertices
        self.edge = edge

    def contract(self, other):
        """
            连接两个顶点
        """
        #合并顶点
        self.vertices += other.vertices
        #加入两顶点不重合的边
        self.edge = [i for i in self.edge + other.edge if i not in self.vertices]

def cut(graph):
    """
        找寻切割边
    """
    if len(graph) == 2:
        return graph

    random_vertex = random.choice(graph)
    random_edge = random.choice(random_vertex.edge)
    #求出邻接结点
    adj_vertex = [i for i in graph if random_edge in i.vertices][0]

    random_vertex.contract(adj_vertex)

    graph.remove(adj_vertex)

    return cut(graph)

def find_min_cut(graph):
    # graph2 = graph[:]
    cut_graph = cut(graph)
    return len(cut_graph[0].edge)

def main():
    graph = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.strip():
            vertices = [int(x) for x in line.split()]
            head = vertices.pop(0)
            graph.append(Adj([head], vertices))

    print find_min_cut(graph)


if __name__ == '__main__':
    main()
