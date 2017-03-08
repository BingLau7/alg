package utils

import (
	"fmt"
)

type IntHeap []int

// 实现了heap.Interface中组合的sort.Interface接口的Less方法
func (h *IntHeap) Less(i, j int) bool {
	return (*h)[i] < (*h)[j]
}

// 实现了heap.Interface中组合的sort.Interface接口的Swap方法
func (h *IntHeap) Swap(i, j int) {
	(*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

// 实现了heap.Interface中组合的sort.Interface接口的Push方法
func (h *IntHeap) Len() int {
	return len(*h)
}

// 实现了heap.Interface的Pop方法
func (h *IntHeap) Pop() (v interface{}) {
	*h, v = (*h)[:h.Len()-1], (*h)[h.Len()-1]
	return
}

// 实现了heap.Interface的Push方法
func (h *IntHeap) Push(v interface{}) {
	*h = append(*h, v.(int))
}

// 按层来遍历和打印堆数据，第一行只有一个元素，即堆顶元素
func (h IntHeap) PrintHeap() {
	n := 1
	levelCount := 1
	for n <= h.Len() {
		fmt.Println(n-1, n-1+levelCount)
		fmt.Println(h[n-1 : n-1+levelCount])
		n += levelCount
		levelCount *= 2
	}
}
