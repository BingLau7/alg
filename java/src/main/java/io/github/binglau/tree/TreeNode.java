package io.github.binglau.tree;

/**
 * 类TreeNode.java的实现描述：TODO:类实现描述
 *
 * @author bingjian.lbj 2016-09-08 下午11:17
 */
public class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value) {
        this.value = value;
    }

    // 通过层序来建立树
    // 返回根节点
    public static TreeNode build(int[] array) {
        return null;
    }

    // 通过树的根节点打印出树的结构
    // 1
    // 2(1-) 3(1+)
    // 4(2-) 5(2+) 12(3-) 7(3+)
    // 13(4-) 23(5-) 16(5+) 11(7-)
    // 其中括号内的分别是根节点及他们是左子树(-)or右子树(+)
    public static void printTree(TreeNode root) {

    }

}

