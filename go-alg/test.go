package main

import (
	"hashing"
	"fmt"
	"alg"
)

func main() {
	fmt.Println("------------Start-----------")
	//normalHash()
	alg.TestStack()
	//for i := 1; i < 20; i++{
	//	code := crc32.ChecksumIEEE([]byte(fmt.Sprintf("test%d", i)))
	//	if code > 1690090958 && code < 2326977762 {
	//		fmt.Println(i)
	//	}
	//}
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