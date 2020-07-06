package two_hundred

import (
	"fmt"
	"go-leetcode/base"
)

// https://leetcode-cn.com/problems/path-sum/

/**
说明
0. 读题
0.0 二叉树与数字
0.1 根节点到叶子节点的路径数字相加相等等于给定数字

1. 思路

1.0 从上到下，每个节点记录的数字换成 parent + node val。最后判断叶子节点的数字是否与给定数字有相等的
1.1 深度遍历，所有结果相加到了叶子节点判断
1.2 递归减 sum

2. 数据结构/算法
2.0 层序遍历
2.1 深度优先搜索

3. 边界
 */

func HasPathSumRun() {
	root := &base.TreeNode{5,
		&base.TreeNode{4,
			&base.TreeNode{11,
				&base.TreeNode{7, nil, nil},
				&base.TreeNode{2, nil, nil}},
				nil},
		&base.TreeNode{8,
			&base.TreeNode{13, nil, nil},
			&base.TreeNode{4, nil,
				&base.TreeNode{1, nil, nil}}}}
	fmt.Println(hasPathSum(root, 22))
}

func hasPathSum(root *base.TreeNode, sum int) bool {
	// 叶子节点不满足要求
	if root == nil {
		return false
	}
	// 叶子节点
	if root.Left == nil && root.Right == nil {
		return sum - root.Val == 0
	}
	// 递归两边节点
	return hasPathSum(root.Left, sum - root.Val) || hasPathSum(root.Right, sum - root.Val)
}