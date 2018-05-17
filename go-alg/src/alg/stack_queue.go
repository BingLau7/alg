package alg


/**
两个栈模拟队列操作
 */

type StackQueue struct {
	s1 Stack
	s2 Stack
}

func StackQueueNew() *StackQueue {
	return &StackQueue{
		s1: StackNew(),
		s2: StackNew(),
	}
}

func(sq *StackQueue) Push(data interface{}) {
	push_all_to_other(sq.s2, sq.s1)
	sq.s1.Push(data)
}

func(sq *StackQueue) Pop() interface{} {
	push_all_to_other(sq.s1, sq.s2)
	return sq.s2.Pop()
}
func push_all_to_other(source Stack, target Stack) {
	for !source.Empty() {
		target.Push(source.Pop())
	}
}

func(sq *StackQueue) Front() interface{} {
	if sq.s1.Empty() && !sq.s2.Empty() {
		push_all_to_other(sq.s2, sq.s1)
	}
	return sq.s1.Peek()
}

func(sq *StackQueue) Empty() bool {
	return sq.s1.Empty() && sq.s2.Empty()
}

func(sq *StackQueue) Size() int {
	return sq.s1.Size() + sq.s2.Size()
}