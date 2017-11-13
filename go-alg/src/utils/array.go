package utils

func RemoveSliceIntIndex(s []int, i int) []int{
	return append(s[:i],s[i+1:]...)
}

func SwapArrayNum(arr []int, i int, j int) {
	tmp := arr[i]
	arr[i] = arr[j]
	arr[j] = tmp
}
