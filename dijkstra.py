# encoding:utf-8

"""
The file contains an adjacency list representation of an undirected weighted
graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples
that are adjacent to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry indicating that this row
corresponds to the vertex labeled 6. The next entry of this row "141,8200"
indicates that there is an edge between vertex 6 and vertex 141 that has length
8200. The rest of the pairs of this row indicate the other vertices adjacent
to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1
(the first vertex) as the source vertex, and to compute the shortest-path
distances between 1 and every other vertex of the graph. If there is no path
between a vertex v and vertex 1, we'll define the shortest-path distance
between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices,
in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances
as a comma-separated string of integers. So if you find that all ten of these
vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000
distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,
1000,1000,1000. Remember the order of reporting DOES MATTER, and the string
should be in the same order in which the above ten vertices are given. Please
type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward
O(mn) time implementation of Dijkstra's algorithm should work fine. OPTIONAL:
For those of you seeking an additional challenge, try implementing the
heap-based version. Note this requires a heap that supports deletions, and
you'll probably need to maintain some kind of mapping between vertices and
their positions in the heap.
"""

import sys
import heapq

INF = float('INF')  #无穷大
UNDEFINED = -1      #无此结点

class Vertex(object):
    """
        顶点类
    """
    def __init__(self, vertex):
        self.vertex = vertex
        self.distance = INF     #某源点到vertex的最短距离，主要是提供给dijkstra使用

    def __eq__(self, other):
        return self.vertex == other.vertex

    def __str__(self):
        return '第' + str(self.vertex) + '结点'

class Edge(object):
    """
        边类
        enter_vertex为入度
        out_vertex为出度
    """
    def __init__(self, vertex_v, vertex_u, weighted):
        self.weighted = weighted
        self.enter_vertex = vertex_v
        self.out_vertex = vertex_u

    def __str__(self):
        return str(self.enter_vertex) + ' -> ' \
                + str(self.out_vertex) + '，权重：' \
                + str(self.weighted)

class Graph(object):
    """
        图类，邻接表表示
    """
    def __init__(self):
        """
            vertices:图中包含的顶点,key为顶点标记值
            edges:边,其中edges[Vertex.vertex]代表vertex代表vertex顶点的邻接边
        """
        self.vertices = {}
        self.edges = {}

    def add_edge(self, vertex_v, vertex_u, weighted):
        """
            添加边的时候需要查看是否有未创建的结点，
            如果有需要添加结点
        """
        vertex_v = Vertex(vertex_v)
        vertex_u = Vertex(vertex_u)

        if vertex_v not in self:
            self._add_vertex(vertex_v)
        if vertex_u not in self:
            self._add_vertex(vertex_u)

        edge = Edge(vertex_v, vertex_u, weighted)


        if vertex_v.vertex in self.edges:
            self.edges[vertex_v.vertex].append(edge)
        else:
            self.edges.update({vertex_v.vertex:[edge]})

        #需判断edges的容量并按需求添加容量
        max_vertex = max(vertex_v.vertex, vertex_u.vertex)
        if max(self.edges) < max_vertex:
            self.edges[max_vertex] = []


    def _add_vertex(self, vertex):
        """
            添加顶点
        """
        self.vertices[vertex.vertex] = vertex

    def get_edges(self, vertex):
        """
            获得vertex的邻接边
        """
        if type(vertex) == Vertex:
            return self.edges[vertex.vertex]
        elif type(vertex) == int:
            return self.edges[vertex]

    def get_vertex(self, vertex):
        """
            获得图中值为vertex的顶点
        """
        assert vertex in self.vertices.iterkeys(), '无此结点'
        return self.vertices[vertex]

    def get_vertices(self):
        """
            获得所有顶点
        """
        return list(self.vertices.itervalues())

    def __contains__(self, vertex):
        return vertex in self.vertices.itervalues()

    def print_graph(self):
        """
            打印图
        """
        for vertex in self.vertices.itervalues():
            for edge in self.get_edges(vertex):
                print edge


def dijkstra(graph, source):
    """
        graph:图
        source:起始点，int类型
    """
    pervious = {}   #前驱结点

    #初始化
    for vertex in graph.vertices:
        graph.get_vertex(vertex).distance = INF
        pervious[graph.get_vertex(vertex)] = UNDEFINED

    graph.get_vertex(source).distance = 0

    #集合 know_vertex 保留了我们已知的所有 distance[v] 的值已经是最短路径的值顶点
    know_vertex = []
    #集合 unknow_vertex 则保留其他所有顶点。
    unknow_vertex = graph.get_vertices()

    while unknow_vertex:
        enter_vertex = heapq.nsmallest(1, unknow_vertex, key=lambda x:x.distance).pop()
        unknow_vertex.remove(enter_vertex)
        know_vertex.append(enter_vertex)
        for edge in graph.get_edges(enter_vertex):
            if graph.get_vertex(edge.out_vertex.vertex).distance > \
                    graph.get_vertex(edge.enter_vertex.vertex).distance + edge.weighted:
                        graph.get_vertex(edge.out_vertex.vertex).distance = \
                                graph.get_vertex(edge.enter_vertex.vertex).distance + edge.weighted

                        pervious[graph.get_vertex(edge.out_vertex.vertex)] \
                                = graph.get_vertex(edge.enter_vertex.vertex)

    return pervious

def get_shortest_path(vertex, pervious):
    """
        得到source到vertex的最短路径，perviouse是dijkstra所得
    """
    path = []
    tmp_vertex = vertex
    while pervious[tmp_vertex] != UNDEFINED:
        path.append(tmp_vertex)
        tmp_vertex = pervious[tmp_vertex]

    return path


def main():
    """
        测试函数
    """
    graph = Graph()

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip().split(' ')
        vertex_v = line.pop(0)
        for edge in line:
            edge = edge.split(',')
            graph.add_edge(int(vertex_v), int(edge[0]), int(edge[1]))


    # graph.print_graph()
    pervious = dijkstra(graph, 1)
    vertices = [vertex for vertex in graph.vertices]
    # for vertex in vertices:
    #     print vertex, graph.get_vertex(vertex).distance,
    #     print '[',
    #     shortest_path = get_shortest_path(graph.get_vertex(vertex), pervious)
    #     while shortest_path:
    #         print shortest_path.pop(),
    #     print ']'

    test = '7,37,59,82,99,115,133,165,188,197'.split(',')
    for vertex in test:
        vertex = int(vertex)
        # print vertex, graph.get_vertex(vertex).distance
        # print '[',
        # shortest_path = get_shortest_path(graph.get_vertex(vertex), pervious)
        # while shortest_path:
        #     print shortest_path.pop(),
        # print ']'
        print graph.get_vertex(vertex).distance,

if __name__ == '__main__':
    main()
