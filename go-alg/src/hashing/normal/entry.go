package normal

import (
	"hash/fnv"
)

type Entry struct {
	key string
}
func (entry *Entry) HashCode() uint32 {
	h := fnv.New32()
	h.Write([]byte(entry.key))
	return h.Sum32()
}

func (entry *Entry)Equal(otherEntry Entry) bool {
	if otherEntry.key == entry.key {
		return true
	}
	return false
}

func (entry *Entry) String() string {
	return entry.key
}

func InitEntry(key string) *Entry {
	return &Entry{key: key}
}
