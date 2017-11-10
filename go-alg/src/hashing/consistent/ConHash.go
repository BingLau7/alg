package consistent


import (
	"fmt"
	"hash/crc32"
	"strconv"
	"sort"
)

type HashFunc func(date []byte) uint32
type HashRing []uint32

func(r HashRing) Len() int { return len(r) }
func(r HashRing) Less(i, j int) bool { return r[i] < r[j] }
func(r HashRing) Swap(i, j int) { r[i], r[j] = r[j], r[i] }

type ConHash struct {
	hashFunc     HashFunc
	hashRing     HashRing
	vNodes       int
	nodeMapNum   map[string] int    // physical node---> node num
	vNodeMapNode map[uint32] string // vNode key ---->physical node

}


func ConHashNew() *ConHash {
	return &ConHash {
		hashFunc:     crc32.ChecksumIEEE,
		hashRing:     HashRing{},
		vNodes:       0,
		nodeMapNum:   make(map[string] int),
		vNodeMapNode: make(map[uint32] string),
	}
}

func (ch *ConHash) NodeHash(data []byte) uint32 {
	return ch.hashFunc(data)
}

// vNode format: "n_name_%d"
func (ch *ConHash) NodeAdd(n_name string, vn_num int) {
	var name string
	var key uint32
	if _,ok := ch.nodeMapNum[n_name]; ok {
		fmt.Println("node", n_name, "already exist")
		return
	}
	ch.nodeMapNum[n_name] = vn_num
	for i := 0; i < vn_num; i++ {
		name = n_name + "_" + strconv.Itoa(i)
		key = ch.NodeHash([]byte(name))
		ch.vNodeMapNode[key] = n_name
		ch.hashRing = append(ch.hashRing, key)
		ch.vNodes++
	}
	sort.Sort(ch.hashRing)
}

func (ch *ConHash) NodeRemove(n_name string) {
	var name string
	var key uint32

	if _,ok := ch.nodeMapNum[n_name]; !ok {
		fmt.Println("node", n_name, "not exist")
	}

	vNode_num := ch.nodeMapNum[n_name]
	for i := 0; i < vNode_num; i++ {
		name = n_name + "_" + strconv.Itoa(i)
		key = ch.NodeHash([]byte(name))
		for i,v := range ch.hashRing {
			if v == key {
				ch.hashRing = append(ch.hashRing[:i], ch.hashRing[i+1:]...)
			}
		}
		delete(ch.vNodeMapNode, key)
		ch.vNodes--
	}
	delete(ch.nodeMapNum, n_name)
}


func (ch *ConHash) NodeLookup(object string) string {
	var key uint32
	var hitIndex int

	key = ch.NodeHash([]byte(object))
	index := sort.Search(len(ch.hashRing), func(i int) bool { return ch.hashRing[i] >= key })
	if index == len(ch.hashRing) {
		hitIndex = 0
	} else {
		hitIndex = index
	}
	hitKey := ch.hashRing[hitIndex]
	node, _ := ch.vNodeMapNode[hitKey]
	return node
}

func (ch *ConHash) NodeGetVNodes() int {
	return ch.vNodes
}
