package main

import (
	"fmt"
	"alg"
)

func main() {
	fmt.Println("------------Start-----------")
	tree := alg.TreeNewAssign([]int{1, nil, 2, 3})
	fmt.Println(tree)
	fmt.Println("------------End-----------")
}
