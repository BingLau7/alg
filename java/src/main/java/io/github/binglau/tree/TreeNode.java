package io.github.binglau.tree;

import apple.laf.JRSUIUtils;

import java.util.LinkedList;

/**
 * 类TreeNode.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-08 下午11:17
 */
public class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;
    int size = 0;

    public TreeNode(int value) {
        this.value = value;
    }

    // 通过层序来建立树
    // 返回根节点
    public static TreeNode build(int[] array) {
        if (array.length <= 0) return null;
        TreeNode root = new TreeNode(array[0]);
        for (int i = 1; i < array.length; i++) {
            root.add(array[i]);
        }
        return root;
    }

    // 通过树的根节点打印出树的结构
    // 1
    // 2(1-) 3(1+)
    // 4(2-) 5(2+) 12(3-) 7(3+)
    // 13(4-) 23(5-) 16(5+) 11(7-)
    // 其中括号内的分别是根节点及他们是左子树(-)or右子树(+)
    public static void printTree(TreeNode root) {
        if (root == null) {
            System.out.println("the tree is empty");
            return;
        }
        // 使用队列实现 BSF
        java.util.Queue<TreeNode> queue = new LinkedList();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            System.out.println(node.value);
            if (node.left != null) queue.add(node.left);
            if (node.right != null) queue.add(node.right);
        }
    }

    private TreeNode add(int value) {
        if (this.left == null) {
            TreeNode node = new TreeNode(value);
            this.left = node;
            this.size++;
            return node;
        }
        else if (this.right == null){
            TreeNode node = new TreeNode(value);
            this.right = node;
            this.size++;
            return node;
        } else {
            if (this.right.size < this.left.size) return this.right.add(value);
            else return this.left.add(value);
        }
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6};
        TreeNode root = build(array);
        printTree(root);
    }

}

