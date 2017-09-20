package io.github.binglau.interview;

import io.github.binglau.tree.TreeNode;

/**
 * 类RebuildTree.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-12-23 下午7:18
 */
public class RebuildTree {

    public static TreeNode rebuildTree(int[] preOrder, int start,
                                 int[] inOrder, int end, int length) {
        //参数验证
        if (preOrder == null || preOrder.length == 0 || inOrder == null
                || inOrder.length == 0 || length <= 0) {
            return null;
        }

        //建立子树根节点
        int value = preOrder[start];
        TreeNode root = new TreeNode(value);

        //递归终止条件：子树只有一个节点
        if (length == 1)
            return root;

        //分拆子树的左子树和右子树
        int i = 0;
        while (i < length && value != inOrder[end - i]) {
            i++;
        }

        //建立子树的左子树
        root.left = rebuildTree(preOrder, start + 1, inOrder, end - i - 1, length - 1 - i);
        //建立子树的右子树
        root.right = rebuildTree(preOrder, start + length - i, inOrder, end, i );

        return root;
    }

    public static void main(String[] args) {
        int[] preOrders = {1, 2, 4, 8, 9, 5, 3, 6, 7};
        int[] inOrders = {8, 4, 9, 2, 5, 1, 6, 3, 7};
        TreeNode root = rebuildTree(preOrders, 0, inOrders, inOrders.length - 1, inOrders.length);
        TreeNode.printTree(root);
    }
}
