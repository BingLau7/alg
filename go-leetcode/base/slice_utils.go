package base

func ReverseInt(nums []int) []int {
	if nums == nil || len(nums) == 0 {
		return nums
	}
	var res []int
	for i := len(nums) - 1; i >= 0; i-- {
		res = append(res, nums[i])
	}
	return res
}
