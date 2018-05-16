package alg

import "fmt"

type Stack struct {
	data []interface{}
}

func StackNew() *Stack {
	return &Stack{
		data:make([]interface{}, 0),
	}
}

func (s *Stack) Pop() interface{} {
	size := s.Size()
	if size == 0 {
		return nil
	}
	r := s.data[size - 1]
	s.data = s.data[:size - 1]
	return r
}

func (s *Stack) Push(data interface{}) {
	s.data = append(s.data, data)
}

func (s *Stack) Size() int {
	return len(s.data)
}

func (s *Stack) Peek() interface{} {
	size := s.Size()
	if size == 0 {
		return nil
	}
	return s.data[size - 1]
}

func TestStack() {
	stack := StackNew()
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
