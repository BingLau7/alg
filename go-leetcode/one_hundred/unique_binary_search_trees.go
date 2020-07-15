package one_hundred

import "fmt"

// https://leetcode-cn.com/problems/unique-binary-search-trees/

func RunNumTrees() {
	fmt.Println(numTrees(3))
}


/**
说明:

0. 读题
	符合搜索二叉树

1. 思路
	错误思路，无法确定满节点如何计算：
	3 的数量应该是在 2 的数量记录上再找到合适的位置（头，中间节点，尾部）？
	头结点 1 + 只要不是满节点即可 + 1
	正确思路：给定一个有序序列 1...n，为了构建出一棵二叉搜索树，
			我们可以遍历每个数字 i，将该数字作为树根，将 1...(i-1) 序列作为左子树，将 (i+1)...n 序列作为右子树。
			接着我们可以按照同样的方式递归构建左子树和右子树。
	在上述构建的过程中，由于根的值不同，因此我们能保证每棵二叉搜索树是唯一的。

2. 数据结构、算法
	动态规划
	F(i,n) 表示以 i 为节点的数量
	G(n) 表示 n 的所有搜索树的数量
	F(i,n) = G(i - 1) * G(n - i) 表示 i 为根节点数量是左边子树的数量集合 * 右边子树的数量集合
	G(n) = F(0,n) + ... F(i,n) + ... F(n,n)
	G(n) = G(0) * G(n-1) + ... G(i-1) + G(n-i) ... + G(n-1) * G(0)

3. 边界

4. 总结
*/
func numTrees(n int) int {
	g := make([]int, n + 1)
	g[0], g[1] = 1, 1
	for m := 2; m <= n; m++ { // m 指节点数量
		for i := 1; i <= m; i++ { // i 指根节点
			g[m] += g[i-1] * g[m-i]
		}
	}
	return g[n]
}
