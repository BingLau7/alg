package io.github.binglau;

import io.github.binglau.tree.BSTIterator;
import io.github.binglau.tree.BinarySearchTree;
import io.github.binglau.tree.TreeNode;
import org.junit.Test;

/**
 * 类TreeTest.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-08 下午10:44
 */
public class TreeTest {
    public TreeNode createBST() {
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
        return BST.root;
    }

    @Test
    public void createTest() {
        BinarySearchTree BST = new BinarySearchTree();
        BST.print(createBST());
    }

    @Test
    public void iteratorTest() {
        BinarySearchTree BST = new BinarySearchTree();
        TreeNode node = createBST();
        BSTIterator bstIterator = new BSTIterator(node);
        while (bstIterator.hasNext()) {
            System.out.println(bstIterator.next());
        }
    }
}
