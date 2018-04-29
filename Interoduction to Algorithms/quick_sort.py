def paritition(nums, left, right):
    p = nums[left]
    i = left + 1
    j = i
    while j <= right:
        if nums[j] < p:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums[left], nums[i-1] = nums[i-1], nums[left]
    return i-1


def quick_sort(nums, left, right):
    if right == left:
        return
    mid = paritition(nums, left, right)
    quick_sort(nums, left, mid)
    quick_sort(nums, mid+1, right)


if __name__ == '__main__':
    nums = [5, 4, 9, 8, 11, 1, 20, 3]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)
