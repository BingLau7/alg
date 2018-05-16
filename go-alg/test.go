package main

import (
	"hashing"
	"fmt"
	"alg"
)

func main() {
	fmt.Println("------------Start-----------")

	alg.TestSimpleQueue([]int{1, 2, 3, 4, 5})
	fmt.Println("------------End-----------")
}

func normalHash() {
	hashing.TestNormal()
}

type A interface {
	S()
}

type B struct {
	name string
}

func (b *B) S() {
	fmt.Println(b.name)
}

func test(a A) {
	if e, ok := a.(*B); ok {
		fmt.Println(e.name)
	}
	a.S()
}