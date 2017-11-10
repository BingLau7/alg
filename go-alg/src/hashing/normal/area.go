package normal

import "hash/fnv"

type Area struct {
	name string
	entries map[Entry]Entry
}

func (area *Area) put(e Entry) {
	area.entries[e] = e
}

func (area *Area) get(e Entry) Entry {
	return area.entries[e]
}

func InitArea(name string) Area {
	return Area{name:name, entries:make(map[Entry]Entry)}
}

func (area *Area) hashCode() uint32 {
	h := fnv.New32a()
	h.Write([]byte(area.name))
	return h.Sum32()
}
