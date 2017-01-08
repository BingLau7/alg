package io.github.binglau.tree;

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
    TreeNode parent;
    boolean isLeft = true;
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
    // 2(1l) 3(1r)
    // 4(2l) 5(2r) 12(3l) 7(3r)
    // 13(4l) 23(5r) 16(5l) 11(7r)
    // 其中括号内的分别是根节点及他们是左子树(-)or右子树(+)
    public static void printTree(TreeNode root) {
        if (root == null) {
            System.out.println("the tree is empty");
            return;
        }
        // 计数器，辅助计算是否要换行
        int i = 0;
        // 层数
        int k = 1;
        // 使用队列实现 BSF
        java.util.Queue<TreeNode> queue = new LinkedList();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            String dirLabel = "r";
            if (!node.isLeft) dirLabel = "r";
            if (node.parent != null) System.out.print(node.value + "(" + node.parent.value + dirLabel + ") ");
            else System.out.print(node.value + " ");
            i++;
            if (i == (Math.pow(2, k) - 1)) {
                System.out.println();
                k++;
            }
            if (node.left != null) queue.add(node.left);
            if (node.right != null) queue.add(node.right);
        }
    }

    private TreeNode add(int value) {
        if (this.left == null) {
            TreeNode node = new TreeNode(value);
            this.left = node;
            this.size++;
            node.isLeft = true;
            node.parent = this;
            return node;
        }
        else if (this.right == null){
            TreeNode node = new TreeNode(value);
            this.right = node;
            this.size++;
            node.isLeft = false;
            node.parent = this;
            return node;
        } else {
            if (this.left.size < 2) return this.left.add(value);
            else if (this.right.size < this.left.size) return this.right.add(value);
            else return this.left.add(value);
        }
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        TreeNode root = build(array);
        printTree(root);
    }
}
