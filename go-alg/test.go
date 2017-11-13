package main

import (
	"hashing"
	"fmt"
)

func main() {
	fmt.Println("------------Start-----------")
	normalHash()
	//b := &B{name:"123"}
	//test(b)
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