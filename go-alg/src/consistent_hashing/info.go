package consistent_hashing

import "fmt"

/**
参考文章
http://afghl.github.io/2016/07/04/consistent-hashing.html
http://afghl.github.io/2016/11/19/implement-consistent-hashing.html
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

func TestNormal() {
	c := createCluster()
	entries := []Entry{
		{"i"},
		{"have"},
		{"a"},
		{"pen"},
		{"an"},
		{"apple"},
		{"applepen"},
		{"pineapple"},
		{"pineapplepen"},
		{"PPAP"}}

	for _, e := range entries {
		c.Put(e)
	}

	c.AddArea(InitArea("192.168.0.6"))
	findEntries(c, entries)
}

func createCluster() Cluster {
	c := InitCluster()
	c.AddArea(InitArea("192.168.0.0"))
	c.AddArea(InitArea("192.168.0.1"))
	c.AddArea(InitArea("192.168.0.2"))
	c.AddArea(InitArea("192.168.0.3"))
	c.AddArea(InitArea("192.168.0.4"))
	c.AddArea(InitArea("192.168.0.5"))
	return c
}

func findEntries(c Cluster, entries []Entry) {
	for _, e := range entries {
		if e == c.Get(e) {
			fmt.Printf("重新找到 entry: %s\n", e)
		} else {
			fmt.Printf("entry 已失效: %s\n", e)
		}
	}
}