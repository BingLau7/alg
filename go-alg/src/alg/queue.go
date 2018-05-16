package alg

import "fmt"

type Queue interface {
	Push(interface{})
	Pop() interface{}
	Front() interface{}
	Empty() bool
	Size() int
}

type SimpleQueue struct {
	data []interface{}
}

func SimpleQueueNew() *SimpleQueue {
	return &SimpleQueue{
		data: make([]interface{}, 0),
	}
}

func (q *SimpleQueue) Push(data interface{}) {
	q.data = append(q.data, data)
}

func (q *SimpleQueue) Pop() interface{} {
	if q.Empty() {
		return nil
	}
	r := q.Front()
	q.data = q.data[1:]
	return r
}

func (q *SimpleQueue) Front() interface{} {
	if q.Empty() {
		return nil
	}
	return q.data[0]
}

func (q *SimpleQueue) Empty() bool {
	return q.Size() <= 0
}

func (q *SimpleQueue) Size() int {
	return len(q.data)
}

func TestSimpleQueue(arr []int) {
	queue := SimpleQueueNew()
	for i := range arr {
		queue.Push(i)
	}
	fmt.Println(queue.Front())
	for range arr {
		fmt.Printf("%d\n", queue.Pop())
	}
}

/**
两个栈模拟队列操作
 */
func StackMockQueue() {

}