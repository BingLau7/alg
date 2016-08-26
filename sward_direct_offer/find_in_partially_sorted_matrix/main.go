package main

import (
	"fmt"
)

func find(arr [][]int, element int) {
	x_len := len(arr)
	if x_len == 0 {
		return
	}
	y_len := len(arr[0])
	if y_len == 0 {
		return
	}
	search_row_right := x_len
	search_col_down := y_len
	search_row_left := x_len
	search_col_up := y_len
	if element < arr[0][0] || element > arr[x_len][y_len] {
		return
	}
}

func main() {
	arr := [][]int{
		{1, 2, 8, 9},
		{2, 4, 9, 12},
		{4, 7, 10, 13},
		{6, 8, 11, 15},
	}

	find(arr, 7)
}
