package main

import (
	"hashing"
	"fmt"
)

func main() {
	fmt.Println("------------Start-----------")
	normalHash()
	fmt.Println("------------End-----------")
}

func normalHash() {
	hashing.TestNormal()
}
