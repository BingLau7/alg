package io.github.binglau.graph;

import com.google.common.graph.Graph;
import com.google.common.graph.GraphBuilder;
import com.google.common.graph.MutableGraph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

/**
 * 文件描述: 广度优先算法
 1. 访问初始结点v并标记结点v为已访问。
 2. 结点v入队列
 3. 当队列非空时，继续执行，否则算法结束。
 4. 出队列，取得队头结点u。
 5. 查找结点u的第一个邻接结点w。
 6. 若结点u的邻接结点w不存在，则转到步骤3；否则循环执行以下三个步骤：
    1). 若结点w尚未被访问，则访问结点w并标记为已访问。
    2). 标记为已访问。
    3). 查找结点u的继w邻接结点后的下一个邻接结点w，转到步骤6。
 */

public class BFS {
    private static Node initNode = new Node(1);

    public static void bfs(Graph<Node> graph) {
        LinkedList<Node> queue = new LinkedList<>();
        List<Node> nodeVisitList = new ArrayList<>();
        // 访问初始节点并标记为已访问入队列
        initNode.setVisit(true);
        queue.push(initNode);
        nodeVisitList.add(initNode);

        // 当队列非空时执行算法
        while (queue.size() != 0) {
            Node n = queue.pollLast();
            Set<Node> nodes = graph.adjacentNodes(n);
            for (Node nn : nodes) {
                if (!nn.isVisit()) {
                    nn.setVisit(true);
                    queue.push(nn);
                    nodeVisitList.add(nn);
                }
            }
        }

        System.out.println(nodeVisitList);
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

        bfs(graph);
    }
}
