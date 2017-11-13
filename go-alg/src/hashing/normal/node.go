package normal

type Node struct {
	name string
	entries []Entry
}

func (normalNode *Node) Put(entry Entry) {
	normalNode.entries = append(normalNode.entries, entry)
}

func (normalNode *Node) Pop(entry Entry) {
	for i, v := range normalNode.entries {
		if v.Equal(entry) {
			normalNode.entries = append(normalNode.entries[:i], normalNode.entries[i+1:]...)
		}
	}
}

func (normalNode *Node) Get(entry Entry) *Entry {
	for _, v := range normalNode.entries {
		if v.Equal(entry) {
			return &entry
		}
	}
	return nil
}

func (normalNode *Node) Equal(node Node) bool {
	if node.name == normalNode.name {
		return true
	}
	return false
}

func InitNode(name string) *Node {
	return &Node {
		name: name,
	}
}
