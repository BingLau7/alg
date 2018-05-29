package alg

import "fmt"

/**
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
 */
func (tree *Tree) LevelOrder() [][]int {
	result := make([][]int, 0)
	if tree == nil {
		return result
	}
	queue := SimpleQueueNew()
	queue.Push(tree)
	for !queue.Empty() {
		r := make([]int, 0)
		qSize := queue.Size()
		for i := 0; i < qSize; i++ {
			node := queue.Pop().(*Tree)
			r = append(r, node.Value)
			if node.Left != nil {
				queue.Push(node.Left)
			}
			if node.Right != nil { queue.Push(node.Right)
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

/**
https://leetcode.com/problems/binary-tree-preorder-traversal/description/
递归
这个由于使用了全局变量不能通过 leetcode
 */
var result = make([]int, 0)
func (tree *Tree) PreOrderTraversalRecursion() []int {
	if tree == nil {
		return result
	}
	result = append(result, tree.Value)
	tree.Left.PreOrderTraversalRecursion()
	tree.Right.PreOrderTraversalRecursion()
	return result
}

/**
https://leetcode.com/problems/binary-tree-preorder-traversal/description/
循环
 */
func (tree *Tree) PreOrderTraversalLoop() []int {
	result := make([]int, 0)
	stack := SimpleStackNew()
	if tree == nil {
		return result
	}
	stack.Push(tree)
	for !stack.Empty() {
		t := stack.Pop().(*Tree)
		result = append(result, t.Value)
		if t.Right != nil {
			stack.Push(t.Right)
		}
		if t.Left != nil {
			stack.Push(t.Left)
		}
	}
	return result
}

func TestPreOrderTraversal() {
	tree := TreeNewRandom(20)
	levelResult := tree.LevelOrder()
	result := tree.PreOrderTraversalLoop()
	fmt.Println(levelResult)
	fmt.Println(result)
}

func (tree *Tree) InOrderTraversalRecursion() []int {
	if tree == nil {
		return result
	}
	tree.Left.InOrderTraversalRecursion()
	result = append(result, tree.Value)
	tree.Right.InOrderTraversalRecursion()
	return result
}



func (tree *Tree) InOrderTraversalLoop() []int {
	return nil
}

func TestInOrderTraversal(){
	tree := TreeNewRandom(8)
	levelResult := tree.LevelOrder()
	fmt.Println(levelResult)
	tree.InOrderTraversalRecursion()
	fmt.Println(result)
}
