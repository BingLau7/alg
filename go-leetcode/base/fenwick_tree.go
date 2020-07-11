package base

type FenwickTree struct {
	size int
	tree []int
}

func NewFenwickTree(n int) *FenwickTree {
	res := make([]int, n + 1)
	return &FenwickTree{
		size : n,
		tree : res,
	}
}

func (fTree *FenwickTree) lowbit(index int) int {
	return index & (-index)
}

func (fTree *FenwickTree) Update(index int, delta int) {
	for index <= fTree.size {
		fTree.tree[index] += delta
		index += fTree.lowbit(index)
	}
}

func (fTree *FenwickTree) Query(index int) int {
	res := 0
	for index > 0 {
		res += fTree.tree[index]
		index -= fTree.lowbit(index)
	}
	return res
}
