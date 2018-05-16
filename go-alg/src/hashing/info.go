package hashing

import (
	"hashing/normal"
	"hashing/consistent"
	"fmt"
)

/**
参考文章
http://afghl.github.io/2016/07/04/consistent-hashing.html
http://afghl.github.io/2016/11/19/implement-consistent-hashing.html
http://royluo.org/2016/02/25/conhash/
 */

/**
传统 hash 方法是算出一个 object 的 hash 值然后与对应的 hash 空间（以下称 area）数量求余放入相应的 area 中
当 area 数量变换时候 object 的位置几乎要全变换
 */

/**
基本思路:
1. 把 object 求 hash（hash(object) 得到一个数字）；
2. 把 area 也求 hash，然后把 object 和 area 的 hash 值放入一个 hash 空间，
   通过一定的规则决定每个 object 落在哪一个 area 中。
 */

func TestConHash() {
	node1 := consistent.NodeNew("test1")
	node2 := consistent.NodeNew("test2")
	node3 := consistent.NodeNew("test3")
	ch := consistent.ConHashNew()
	var nodes = make([]*consistent.Node, 0)
	nodes = append(nodes, node1)
	nodes = append(nodes, node2)
	nodes = append(nodes, node3)
	ch.NodeInit(nodes)
	for i := 1; i < 10; i++ {
		data := consistent.DataNew(fmt.Sprintf("test %d", i), fmt.Sprintf("val %d", i))
		ch.DataAdd(data)
	}
	ch.DebugPrint()
	data := ch.DataLookup("test 5")
	fmt.Println(data)
	ch.DataRemove("test 5")
	ch.DebugPrint()
	ch.NodeRemove("test2")
	ch.DebugPrint()
}

func TestNormal() {
	entries := []normal.Entry {
		*normal.InitEntry("1"),
		*normal.InitEntry("2"),
		*normal.InitEntry("3"),
		*normal.InitEntry("4"),
		*normal.InitEntry("9"),
		*normal.InitEntry("12"),
		*normal.InitEntry("33"),
	}

	h := normal.InitHash()
	h.AddNode(*normal.InitNode("01"))
	//h.AddNode(*normal.InitNode("02"))
	//h.AddNode(*normal.InitNode("03"))
	//h.AddNode(*normal.InitNode("04"))

	for _, e := range entries {
		h.Put(e)
	}

	h.AddNode(*normal.InitNode("05"))
}
