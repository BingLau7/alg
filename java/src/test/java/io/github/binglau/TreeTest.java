package io.github.binglau;

import io.github.binglau.tree.BinarySearchTree;
import org.junit.Test;

/**
 * 类TreeTest.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-08 下午10:44
 */
public class TreeTest {
    @Test
    public void createBST() {
        BinarySearchTree BST = new BinarySearchTree();
        BST.insert(20);
        BST.insert(12);
        BST.insert(23);
        BST.insert(28);
        BST.insert(8);
        BST.insert(15);
        BST.insert(14);
        BST.insert(16);
        BST.insert(13);
        BST.print(BST.root);
    }
}
