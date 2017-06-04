package io.github.binglau.graph;

import com.google.common.graph.GraphBuilder;
import com.google.common.graph.MutableGraph;

/**
 * 类Graph.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-11 下午4:39
 */
public class GraphExample {
    public static void main(String[] args) {
        MutableGraph<Integer> graph = GraphBuilder.directed().build();
        graph.putEdge(1 ,2);
        graph.putEdge(2, 3);
        graph.putEdge(2, 4);
        graph.putEdge(2, 5);
        graph.putEdge(5, 1);

        System.out.println(graph);
    }
}
