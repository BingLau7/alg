package main

import (
	"consistent_hashing"
	"fmt"
)

func main() {
	fmt.Println("------------Start-----------")
	normalHash()
	fmt.Println("------------End-----------")
}

func normalHash() {
	consistent_hashing.TestNormal()
}
