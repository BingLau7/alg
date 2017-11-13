package normal

import (
	"fmt"
)

type Hash struct {
	size uint32
	nodes []Node
}

func InitHash() *Hash {
	return &Hash {
		size: 0,
	}
}

func (hash *Hash) getKey(entry Entry) int {
	return int(entry.HashCode() % hash.size)
}

func (hash *Hash) Put(entry Entry) {
	key := hash.getKey(entry)
	hash.nodes[key].Put(entry)
}

func (hash *Hash) Get(entry Entry) *Entry {
	key := hash.getKey(entry)
	return hash.nodes[key].Get(entry)
}

func (hash *Hash) Pop(entry Entry) {
	key := hash.getKey(entry)
	hash.nodes[key].Pop(entry)
}

func (hash *Hash) AddNode(node Node) {
	hash.nodes = append(hash.nodes, node)
	hash.size++
	hash.refresh()
}

func (hash *Hash) RemoveNode(node Node) {
	for i, v := range hash.nodes {
		if v.Equal(node) {
			hash.nodes = append(hash.nodes[:i], hash.nodes[i+1:]...)
			hash.size++
			break
		}
	}
	hash.refresh()
}

func (hash *Hash) refresh() {
	n := 0
	w := 0
	var changeEntries []Entry
	for i, node := range hash.nodes {
		for _, entry := range node.entries {
			w++
			if hash.getKey(entry) != i {
				changeEntries = append(changeEntries, entry)
				node.Pop(entry)
				n++
			}
		}
	}
	fmt.Printf("总数量: %s \n", w)
	fmt.Printf("改变数量: %s \n", n)
	if w != 0 {
		fmt.Printf("改变率 %s \n", n / w)
	}
}
