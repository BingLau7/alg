package io.github.binglau.graph;

import com.google.common.graph.Graph;
import com.google.common.graph.GraphBuilder;
import com.google.common.graph.MutableGraph;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

/**
 * 文件描述: 深度搜索算法

 1. 访问初始结点v，并标记结点v为已访问。
 2. 查找结点v的第一个邻接结点w。
 3. 若w存在，则继续执行4，否则算法结束。
 4. 若w未被访问，对w进行深度优先遍历递归（即把w当做另一个v，然后进行步骤123）。
 5. 查找结点v的w邻接结点的下一个邻接结点，转到步骤3。

 */

class Node {
    int value;
    boolean isVisit;

    public Node(int value) {
        this.value = value;
    }

    public boolean isVisit() {
        return isVisit;
    }

    public void setVisit(boolean visit) {
        isVisit = visit;
    }

    @Override
    public String toString() {
        return "Node{" +
                "value=" + value +
                ", isVisit=" + isVisit +
                '}';
    }
}

public class DFS {
    private static Node initNode = new Node(1);

    public static void dfs(Graph<Node> graph) {
        List<Node> nodeVisitList = new ArrayList<>();
        // 1. 访问初始节点，并标记节点 v 为已访问
        nodeVisitList.add(initNode);
        initNode.setVisit(true);
        dfs(graph, initNode, nodeVisitList);

        System.out.println(nodeVisitList);
    }

    private static void dfs(Graph<Node> graph, Node w, List<Node> nodeVisitList) {
        // 2. 查找相邻节点，并标记为已访问
        for (Node n : graph.adjacentNodes(w)) {
            if (!n.isVisit()) {
                nodeVisitList.add(n);
                n.setVisit(true);
                // 3. 对于未访问的节点遍历它们所有的相邻节点
                dfs(graph, n, nodeVisitList);
            }
        }

    }

    public static void main(String[] args) {
        MutableGraph<Node> graph = GraphBuilder.undirected().build();

        Node n1 = initNode;
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        Node n4 = new Node(4);
        Node n5 = new Node(5);
        Node n6 = new Node(6);
        Node n7 = new Node(7);
        Node n8 = new Node(8);

        graph.putEdge(n1, n2);
        graph.putEdge(n1, n3);

        graph.putEdge(n2, n4);
        graph.putEdge(n2, n5);

        graph.putEdge(n4, n8);

        graph.putEdge(n5, n8);

        graph.putEdge(n3, n6);
        graph.putEdge(n3, n7);

        dfs(graph);
    }
}
