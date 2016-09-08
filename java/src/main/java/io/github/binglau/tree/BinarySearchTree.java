package io.github.binglau.tree;

/**
 * 类BinarySearchTree.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-08 下午9:41
 */
class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value) {
        this.value = value;
    }
}

public class BinarySearchTree {
    public static TreeNode root;

    public TreeNode search(int key) {
        TreeNode current = root;
        while (current != null && key != current.value) {
            if (key < current.value) current = current.left;
            else current = current.right;
        }
        return current;
    }

    public TreeNode insert(int key) {
        TreeNode newNode = new TreeNode(key);
        TreeNode current = root;
        TreeNode parent = null;
        if (current == null) {
            root = newNode;
            return newNode;
        }

        while (true) {
            parent = current;
            if (key < current.value) {
                current = current.left;
                if (current == null) {
                    parent.left = newNode;
                    return newNode;
                }
            } else {
                current = current.right;
                if (current == null) {
                    parent.right = newNode;
                    return newNode;
                }
            }
        }
    }

    /**
     * a.找到删除节点
     * b.如果删除节点左节点为空 , 右节点也为空;
     * c.如果删除节点只有一个子节点 右节点 或者 左节点
     * d.如果删除节点左右子节点都不为空
     */
    public TreeNode delete(int key) {
        TreeNode parent = root;
        TreeNode current = root;
        boolean isLeftChild = false;
        while (current.value != key) {
            parent = current;
            if (current.value > key) {
                isLeftChild = true;
                current = current.left;
            } else {
                isLeftChild = false;
                current = current.right;
            }

            if (current == null) {
                return current;
            }
        }

        if (current.left == null && current.right == null) {
            if (current == root) root = null;
            else if (isLeftChild) parent.left = null;
            else parent.right = null;
        } else if (current.right == null) {
            if (current == root) root = current.left;
            else if (isLeftChild) parent.left = current.left;
            else parent.right = current.left;
        } else if (current.left == null) {
            if (current == root) root = current.right;
            else if (isLeftChild) parent.left = current.right;
            else parent.right = current.right;
        } else {
            TreeNode successor = getDeleteSuccessor(current);
            if (current == root) root = successor;
            else if (isLeftChild) parent.left = successor;
            else parent.right = successor;
            successor.left = current.left;
        }

        return current;
    }

    public TreeNode getDeleteSuccessor(TreeNode deleteNode) {
        TreeNode successor = null;
        TreeNode successorParent = null;
        TreeNode current = deleteNode.right;

        while (current != null) {
            successorParent = successor;
            successor = current;
            current = current.left;
        }

        if (successor != deleteNode.right) {
            successorParent.left = successor.right;
            successor.right = deleteNode.right;
        }

        return successor;
    }

    public void print(TreeNode root) {
        if (root != null) {
            print(root.left);
            System.out.print("value = " + root.value + " ");
            if (root.right != null) System.out.print(" -> ");
            print(root.right);
        }
    }
}
