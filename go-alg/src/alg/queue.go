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

func TestQueue(arr []int) {
	queue := StackQueueNew()
	for i := range arr {
		queue.Push(i)
	}
	fmt.Println(queue.Front())
	fmt.Printf("pop %d\n", queue.Pop())
	fmt.Println(queue.Front())
	queue.Push(20)
	for i := 0; i < 2; i++ {
		fmt.Printf("pop %d\n", queue.Pop())
	}
	fmt.Println(queue.Front())
	queue.Push(20)
	fmt.Printf("pop %d\n", queue.Pop())
	fmt.Println(queue.Front())
	queue.Push(20)
	fmt.Println(queue.Front())
}
