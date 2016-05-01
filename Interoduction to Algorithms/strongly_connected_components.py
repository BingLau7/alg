#!/usr/bin/env python
# encoding: utf-8

"""
The file contains the edges of a directed graph. Vertices are labeled as
positive integers from 1 to 875714. Every row indicates an edge, the vertex
label in first column is the tail and the vertex label in second column is
the head (recall the graph is directed, and the edges are directed from the
first column vertex to the second column vertex). So for example, the 11th
row looks liks : "2 47646". This just means that the vertex with label 2 has
an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing
strongly connected components (SCCs), and to run this algorithm on the given
graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given
graph, in decreasing order of sizes, separated by commas (avoid any spaces).
So if your algorithm computes the sizes of the five largest SCCs to be 500,
400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If
your algorithm finds less than 5 SCCs, then write 0 for the remaining terms.
Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course.
Because of the size of the graph you may have to manage memory carefully.
The best way to do this depends on your programming language and environment,
and we strongly suggest that you exchange tips for doing this on the discussion
forums.
"""
import sys
import constant

sys.setrecursionlimit(1000000)

class Digraph(object):
    def __init__(self, vertices=0, edges=0):
        self.vertices = vertices
        self.edges = edges
        self.explored = []              #被探索过的结点列表
        self.adj = [[] for i in range(vertices)]

    def add_edge(self, v, u):
        if len(self.adj) < v+1:         #0结点保存
            #对于结点的扩张
            n = v - len(self.adj) + 1   #现有结点距离加入的结点还差距n个结点
            for i in range(n):
                self.adj.append([])

            self.vertices += n

        if u not in self.adj[v]:
            self.adj[v].append(u)           #添加邻接边
            self.edges += 1

    def get_v_adj(self, vertex):
        return self.adj[vertex]

    def is_explored(self, vertex):
        if vertex in self.explored:
            return True

    def mark_explored(self, vertex):
        if not self.is_explored(vertex):
            self.explored.append(vertex)

    def print_graph(self):
        for vertex, adj in enumerate(self.adj):
            print vertex, adj

    def reverse(self):
        graph = Digraph(self.vertices, self.edges)
        for i in range(self.vertices):
            for j in self.adj[i]:
                graph.add_edge(j, i)

        return graph


def dfs_loop(graph):
    constant.time = 0
    constant.source = None
    constant.leader = dict()
    constant.finish = dict()
    i = graph.vertices - 1
    while i > 0:
        if not graph.is_explored(i):
            constant.source = i
            dfs(graph, i)
        i -= 1

def dfs_loop_scc(graph, topo):
    constant.time = 0
    constant.source = None
    constant.leader = dict()
    constant.finish = dict()
    for i in topo:
        if not graph.is_explored(i[0]):
            constant.source = i[0]
            dfs(graph, i[0])

def dfs(graph, vertex):
    graph.mark_explored(vertex)
    constant.leader[vertex] = constant.source
    for j in graph.get_v_adj(vertex):
        if not graph.is_explored(j):
            dfs(graph, j)

    constant.time += 1
    constant.finish[vertex] = constant.time

def dfs_nonrecusive(graph, vertex):
    top_stack = [vertex]
    while top_stack:
        # print top_stack
        v = top_stack[-1]
        graph.mark_explored(v)
        constant.leader[v] = constant.source
        children = [u for u in graph.get_v_adj(v) if not graph.is_explored(u)]
        if children:
            for u in children:
                graph.mark_explored(u)
                constant.leader[u] = constant.source
            top_stack += children
        else:
            constant.time += 1
            constant.finish[v] = constant.time
            top_stack.pop()

def in_vertex(vertices, vertex):
    for i in vertices:
        if i == vertex:
            return True
    else:
        return False

def topological_sort(finish):
    return sorted(finish.items(), key=lambda x:x[1], reverse=True)

def ssc(graph):
    graph_reverse = graph.reverse()
    dfs_loop(graph)
    graph_finish = constant.finish
    dfs_loop(graph_reverse)
    graph_reverse_finish = constant.finish

    graph.explored=[]
    dfs_loop_scc(graph, topological_sort(graph_reverse_finish))

    leader_set = set(constant.leader.itervalues())
    scc_num = dict()

    for vertex in constant.leader.itervalues():
        if vertex in leader_set:
            if vertex in scc_num:
                scc_num[vertex] += 1
            else:
                scc_num[vertex] = 1

    print sorted(scc_num.itervalues(), reverse=True)

def main():
    """
        入口
    """
    graph = Digraph()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line=line.strip()
        vertices = [int(x) for x in line.split(' ') if x.isdigit()]
        graph.add_edge(vertices[0]-1, vertices[1]-1)

    ssc(graph)

if __name__ == "__main__":
    main()
