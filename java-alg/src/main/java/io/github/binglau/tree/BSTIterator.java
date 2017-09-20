package io.github.binglau.tree;

/**
 * 类BSTIterator.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-08 下午11:00
 */
public class BSTIterator {
    private BinarySearchTree BST = new BinarySearchTree();
    public BSTIterator(TreeNode node) {
        BST.root = node;
    }

    public boolean hasNext() {
       return BST.root != null;
    }

    public int next() {
        TreeNode nextNode = getMinNode();
        BST.delete(nextNode.value);
        return nextNode.value;
    }

    private TreeNode getMinNode() {
        TreeNode node = BST.root;
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }
}

