package consistent_hashing

import (
	"hash/fnv"
)

type Entry struct {
	Key string
}

func (entry *Entry) hashCode() uint32 {
	h := fnv.New32a()
	h.Write([]byte(entry.Key))
	return h.Sum32()
}

func (entry *Entry) String() string {
	return entry.Key
}
