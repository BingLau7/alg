package io.github.binglau;

import io.github.binglau.tree.RedBlackTree;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

/**
 * 类RedBlackTreeTest.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-11-03 下午2:32
 */
public class RedBlackTreeTest {
    @Test
    public void testPut() {
        Map<String, Integer> map = new HashMap();
        map.put("E", 9);
        map.put("A", 3);
        map.put("R", 123);
        map.put("C", 33);
        map.put("H", 9);
        map.put("X", 3);
        RedBlackTree<String, Integer> tree = putAll(map);
        for (String s: tree.keys()) {
            System.out.println(s + " " + tree.get(s));
        }
    }

    private RedBlackTree putAll(Map<String, Integer> keyValue) {
        RedBlackTree tree = new RedBlackTree();
        for (Map.Entry<String, Integer> entry : keyValue.entrySet()) {
            tree.put(entry.getKey(), entry.getValue());
        }
        return tree;
    }
}
