package alg

import (
	"math/rand"
	"time"
)

type Tree struct {
	Left  *Tree
	Value int
	Right *Tree
	Size int
}

func TreeNewNil() *Tree {
	return nil
}

func TreeNewDefault(k int) *Tree {
	return &Tree{
		Left: nil,
		Value: k,
		Right: nil,
	}
}

func TreeNewAssign(kArr []interface{}) *Tree {
	q := SimpleQueueNew()
	for _, k := range kArr {
		q.Push(k)
	}
	for !q.Empty() {
		t := q.Pop()
		if t == nil {
			continue
		}
		t = t.(*Tree)
	}
	return nil
}

func TreeNewRandom(k int) *Tree {
	rand.Seed(int64(time.Now().Second()))
	maxN := k * 30
	tree := TreeNewDefault(rand.Intn(maxN))
	for i := 0; i < k - 1; i++ {
		tree.BalanceInsert(rand.Intn(maxN))
	}
	return tree
}

func (tree *Tree) BalanceInsert(v int) {
	if tree.Left == nil {
		tree.Left = TreeNewDefault(v)
	} else if tree.Right == nil {
		tree.Right = TreeNewDefault(v)
	} else {
		if tree.Left.Size <= tree.Right.Size {
			tree.Left.BalanceInsert(v)
		} else {
			tree.Right.BalanceInsert(v)
		}
	}
	tree.Size++
}
