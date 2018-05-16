package consistent

import (
	"hash/crc32"
	"fmt"
	"sort"
)

/**
数据结构说明:
1. 为每个 Node 分配一个唯一 key
2. 为每个数据分配一个唯一 key
3. Node 内部又数据结构说明
4. 使用一个有序 map 存储 Node
*/
type Node struct {
	key       string
	hash_code uint32
	data      map[string]*Data
}

func (node *Node) String() string {
	return fmt.Sprintf("key: %s, hash_code: %d. data_size: %d", node.key, node.hash_code, len(node.data))
}

type Data struct {
	key string
	value string
}

func (data *Data) String() string {
	return fmt.Sprintf("key: %s, val: %s", data.key, data.value)
}

type HashFunc func(data []byte) uint32
type HashRing []*Node

func(r HashRing) Len() int {return len(r)}
func(r HashRing) Less(i, j int) bool {return r[i].hash_code < r[j].hash_code }
func(r HashRing) Swap(i, j int) {r[i], r[j] = r[j], r[i]}

type ConHash struct {
	hash_func HashFunc // hash 函数
	hash_ring HashRing // 存储节点
	node_size int // 总共节点数
}

func DataNew(key string, val string) *Data {
	return &Data {
		key: key,
		value: val,
	}
}


func NodeNew(key string) *Node {
	return &Node {
		key:       key,
		hash_code: 0,
		data:      make(map[string]*Data),
	}
}

func ConHashNew() *ConHash {
	return &ConHash{
		hash_func: crc32.ChecksumIEEE,
		hash_ring: HashRing{},
		node_size: 0,
	}
}

/**
节点初始化
初始化:
1. Node 使用 crc32 求出 hash 值
2. map 中存储 hash 值映射 map
 */
func (ch *ConHash) NodeInit(nodes []*Node) {
	for _, node := range nodes {
		ch.NodeAdd(node)
	}
}

/**
节点增加
1. Node 得到 hash 值
2. 只改变顺时针距离最近的的 Node 中的值存储范围
3. 获取最近 Node 的所有数据，重新分配
 */
func (ch *ConHash) NodeAdd(node *Node) {
	if node == nil {
		return
	}
	node.hash_code = ch.hash_func([]byte(node.key));
	ch.hash_ring = append(ch.hash_ring, node)
	ch.node_size++
	sort.Sort(ch.hash_ring)
}

func (ch *ConHash) DebugPrint() {
	fmt.Println("--------- debug")
	for _, node := range ch.hash_ring  {
		fmt.Println(node)
		for k, v := range node.data {
			hash_code := ch.hash_func([]byte(k))
			fmt.Printf("hash code: %d. is less: %d\n", hash_code, node.hash_code - hash_code)
			fmt.Printf("data: %s\n", v)
		}
	}
	fmt.Println("--------- debug end")
}

/**
节点删除
1. 将所有数据存入顺时针距离要删除节点最近的 Node
 */
func (ch *ConHash) NodeRemove(nodeKey string) {
	for i, node := range ch.hash_ring {
		if node.key != nodeKey {
			continue
		}
		ch.hash_ring = append(ch.hash_ring[:i], ch.hash_ring[i+1:]...)
		for _, v := range node.data {
			ch.DataAdd(v)
		}
	}
}

func (ch *ConHash) nodeLookup(data_hash_code uint32) (int, *Node) {
	if ch.hash_ring.Len() == 0 {
		fmt.Println("无节点")
		return -1, nil
	}
	for i, node := range ch.hash_ring {
		if node.hash_code >= data_hash_code {
			return i, node
		}
	}
	return 0, ch.hash_ring[0]
}

/**
数据增加
1. 请求数据对应 hash 值
2. 得到顺时针方向距离数据 hash 值最近的 map (环状)
3. 存储进入 Node
 */
func (ch *ConHash) DataAdd(data *Data) {
	hash_code := ch.hash_func([]byte(data.key))
	_, node := ch.nodeLookup(hash_code)
	if node != nil {
		node.data[data.key] = data
	}
}

/**
数据删除
 */
func (ch *ConHash) DataRemove(dataKey string) {
	hash_code := ch.hash_func([]byte(dataKey))
	_, node := ch.nodeLookup(hash_code)
	if node != nil {
		if _, ok := node.data[dataKey]; ok {
			delete(node.data, dataKey)
		}
	}
}

/**
数据获取
1. 请求数据对应 hash 值
2. 得到顺时针方向距离数据 hash 值最近的 map (环状)
3. 获取 Node 中是否存在 data，存在返回
 */
func (ch *ConHash) DataLookup(dataKey string) *Data {
	hash_code := ch.hash_func([]byte(dataKey))
	_, node := ch.nodeLookup(hash_code)
	if node == nil {
		return nil
	}
	if val, ok := node.data[dataKey]; ok {
		return val
	}
	return nil
}
