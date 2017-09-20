package main

import (
	"alg"
	"fmt"
)

func main() {
	args := [5]string{"2", "1", "+", "3", "*"}
	fmt.Println(alg.EvaluateResversePolishNotation(args[:]))
}
