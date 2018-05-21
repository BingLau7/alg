package alg

import "fmt"

/**
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
 */
func (tree *Tree) LevelOrder() [][]int {
	result := make([][]int, 0)
	queue := SimpleQueueNew()
	queue.Push(tree)
	for !queue.Empty() {
		r := make([]int, 0)
		q_size := queue.Size()
		for i := 0; i < q_size; i++ {
			node := queue.Pop().(*Tree)
			r = append(r, node.Value)
			if node.Left != nil {
				queue.Push(node.Left)
			}
			if node.Right != nil {
				queue.Push(node.Right)
			}
		}
		result = append(result, r)
	}
	return result
}

func TestLevelOrder() {
	tree := TreeNewRandom(6)
	result := tree.LevelOrder()
	fmt.Println(result)
}