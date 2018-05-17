package alg

import "fmt"

type Stack interface {
	Pop() interface{}
	Push(interface{})
	Size() int
	Empty() bool
	Peek() interface{}
}

type SimpleStack struct {
	data []interface{}
}

func StackNew() *SimpleStack {
	return &SimpleStack{
		data:make([]interface{}, 0),
	}
}

func (s *SimpleStack) Pop() interface{} {
	size := s.Size()
	if size == 0 {
		return nil
	}
	r := s.data[size - 1]
	s.data = s.data[:size - 1]
	return r
}

func (s *SimpleStack) Push(data interface{}) {
	s.data = append(s.data, data)
}

func (s *SimpleStack) Size() int {
	return len(s.data)
}

func (s *SimpleStack) Peek() interface{} {
	size := s.Size()
	if size == 0 {
		return nil
	}
	return s.data[size - 1]
}

func (s *SimpleStack) Empty() bool {
	return s.Size() <= 0
}

func TestStack(stack Stack) {
	stack.Push(1)
	stack.Push(3)
	stack.Push(6)
	fmt.Printf("size: %d\n", stack.Size())
	fmt.Printf("peek data: %d\n", stack.Peek())
	fmt.Printf("pop data: %d\n", stack.Pop())
	fmt.Printf("pop data: %d\n", stack.Pop())
	fmt.Printf("pop data: %d\n", stack.Pop())
	fmt.Printf("size: %d\n", stack.Size())
}
