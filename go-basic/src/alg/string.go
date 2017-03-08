package alg

import (
	"fmt"
)

type intHeap []int

func Test() string {
	return "test"
}

// 实现了heap.Interface中组合的sort.Interface接口的Push方法
func (h *intHeap) Len() int {
	return len(*h)
}

// 实现了heap.Interface的Pop方法
func (h *intHeap) Pop() (v interface{}) {
	*h, v = (*h)[:h.Len()-1], (*h)[h.Len()-1]
	return
}

// 实现了heap.Interface的Push方法
func (h *intHeap) Push(v interface{}) {
	*h = append(*h, v.(int))
}

// 按层来遍历和打印堆数据，第一行只有一个元素，即堆顶元素
func (h intHeap) printHeap() {
	n := 1
	levelCount := 1
	for n <= h.Len() {
		fmt.Println(h[n-1 : n-1+levelCount])
		n += levelCount
		levelCount *= 2
	}
}

func EvaluateResversePolishNotation(ops []string) int {
	nums := new(intHeap)
	nums.Push(4)
	nums.Push(3)
	nums.printHeap()
	return 0
}
