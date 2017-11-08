package main

import (
	"fmt"
	"alg"
)

func main() {
	var nums = [] int{10, 1, 2, 7, 6, 1, 5}
	fmt.Println(alg.CombinationSum2(nums, 8))
	//fmt.Println(utils.RemoveSliceInt(nums, len(nums)-1))
}
